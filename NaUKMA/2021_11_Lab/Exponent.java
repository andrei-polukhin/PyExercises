/*
 * Sum sequence s_n = 1 + x + x^2/2 +...+ x^n/n!
 * is approximately equal to e^x if 0 <= x < 1.
 * 
 * The task is to calculate e^x if x in [0; 1)
 * with the precision of a specified epsilon (ep).
 * In other words, abs(s_n - s_(n - 1)) < ep.
 * 
 * Accomplish the goal using both the iterative and recursive approaches.
 */
import acm.program.ConsoleProgram;

public class Exponent extends ConsoleProgram {
	private static final long serialVersionUID = 1L;

	public void run() {
		while (true) {
			// input: fail fast
			double x = readDouble("Enter x: ");
			if (x >= 1 || x < 0) {
				println("x must be in [0; 1)");
				continue;
			}
			double ep = readDouble("Enter ep: ");
			if (ep <= 0) {
				println("ep must be positive");
				continue;
			}

			println("The value of e^x (iterative): " + sumIterative(ep, x));
			println("The value of e^x (recursive): " + sumRecursive(ep, x, 1, 1));
			println("The value of e^x from Math: " + Math.exp(x));
		}
	}

	private double sumIterative(double ep, double x) {
		double sum = 0;
		double sum0 = 0;
		int n = 0;

		while (true) {
			sum0 = sum;
			sum += Math.pow(x, n) / factorial(n);
			n++;
			if (ep > Math.abs(sum - sum0)) {
				// already precise enough
				break;
			}
		}

		return sum;
	}

	private double sumRecursive(double ep, double x, int n, double i) {
		if (ep > i * x / n) {
			// already precise enough
			return 1;
		}

		return i * x / n + sumRecursive(ep, x, n + 1, i * x / n);
	}

	private long factorial(int n) {
		if (n == 0) {
			return 1;
		}
		return n * factorial(n - 1);
	}
}
