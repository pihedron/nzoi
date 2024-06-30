import static java.lang.Math.min;

import java.util.*;

public class Main {
  static class Programmer {
    int h;
    int d;

    public Programmer(int h, int d) {
      this.h = h;
      this.d = d;
    }
  }

  static class House {
    int id;
    int k;

    public House(int id, int k) {
      this.id = id;
      this.k = k;
    }
  }

  public static void main(String[] args) {
    Scanner scanner = new Scanner(System.in);

    int N = scanner.nextInt();
    int X = scanner.nextInt();
    int M = scanner.nextInt();

    Programmer[] programmers = new Programmer[M];
    House[] houses = new House[N];

    for (int i = 0; i < N; i++) {
      houses[i] = new House(i, scanner.nextInt());
    }

    for (int i = 0; i < M; i++) {
      programmers[i] = new Programmer(scanner.nextInt() - 1, scanner.nextInt());
    }

    scanner.close();

    solve(programmers, houses, X);
  }

  static void solve(Programmer[] programmers, House[] houses, int x) {
    final int M = programmers.length;
    final int H = houses.length;

    final int N = M + H + 2;
    final int S = N - 1;
    final int T = N - 2;

    NetworkFlowSolverBase solver;
    solver = new FordFulkersonDfsSolver(N, S, T);

    for (int i = 0; i < M; i++) {
      solver.addEdge(S, i, 1);
    }

    for (int i = 0; i < M; i++) {
      Programmer programmer = programmers[i];
      for (int j = 0; j < H; j++) {
        House house = houses[j];
        if (house.k == 0) continue;
        if (Math.abs(programmer.h - house.id) <= Math.floorDiv(programmer.d, x)) {
          solver.addEdge(i, M + j, 1);
        }
      }
    }

    for (int i = 0; i < H; i++) {
      if (houses[i].k == 0) continue;
      solver.addEdge(M + i, T, houses[i].k);
    }

    solver.solve();

    if (solver.maxFlow == M) {
      System.out.println("SOLUTION IS TRIVIAL");
      for (List<Edge> edges : solver.graph) {
        for (Edge edge : edges) {
          if (!edge.isResidual() && edge.flow > 0 && edge.from != solver.s && edge.to != solver.t) {
            System.out.println(edge.to - M + 1);
          }
        }
      }
    } else {
      System.out.println("SOLUTION IS NON-TRIVIAL");
    }
  }

  private static class Edge {
    public int from, to;
    public Edge residual;
    public long flow;
    public final long capacity;

    public Edge(int from, int to, long capacity) {
      this.from = from;
      this.to = to;
      this.capacity = capacity;
    }

    public boolean isResidual() {
      return capacity == 0;
    }

    public long remainingCapacity() {
      return capacity - flow;
    }

    public void augment(long bottleNeck) {
      flow += bottleNeck;
      residual.flow -= bottleNeck;
    }
  }

  private abstract static class NetworkFlowSolverBase {
    static final long INF = Long.MAX_VALUE / 2;

    final int n, s, t;

    protected int visitedToken = 1;
    protected int[] visited;

    protected boolean solved;

    protected long maxFlow;

    protected List<Edge>[] graph;

    public NetworkFlowSolverBase(int n, int s, int t) {
      this.n = n;
      this.s = s;
      this.t = t;
      initializeEmptyFlowGraph();
      visited = new int[n];
    }

    @SuppressWarnings("unchecked")
    private void initializeEmptyFlowGraph() {
      graph = new List[n];
      for (int i = 0; i < n; i++) graph[i] = new ArrayList<Edge>();
    }

    public void addEdge(int from, int to, long capacity) {
      if (capacity <= 0) throw new IllegalArgumentException("Forward edge capacity <= 0");
      Edge e1 = new Edge(from, to, capacity);
      Edge e2 = new Edge(to, from, 0);
      e1.residual = e2;
      e2.residual = e1;
      graph[from].add(e1);
      graph[to].add(e2);
    }

    private void execute() {
      if (solved) return;
      solved = true;
      solve();
    }
    
    public abstract void solve();
  }

  private static class FordFulkersonDfsSolver extends NetworkFlowSolverBase {
    public FordFulkersonDfsSolver(int n, int s, int t) {
      super(n, s, t);
    }

    @Override
    public void solve() {
      for (long f = dfs(s, INF); f != 0; f = dfs(s, INF)) {
        visitedToken++;
        maxFlow += f;
      }
    }

    private long dfs(int node, long flow) {
      if (node == t) return flow;

      visited[node] = visitedToken;

      List<Edge> edges = graph[node];
      for (Edge edge : edges) {
        if (edge.remainingCapacity() > 0 && visited[edge.to] != visitedToken) {
          long bottleNeck = dfs(edge.to, min(flow, edge.remainingCapacity()));
          if (bottleNeck > 0) {
            edge.augment(bottleNeck);
            return bottleNeck;
          }
        }
      }

      return 0;
    }
  }
}