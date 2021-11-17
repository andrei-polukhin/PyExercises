/*
 * Sum sequence s_n = 1 - x^2 / 2! +...+ (-1)^n * x^(2n) / (2n)!
 * is approximately equal to cos(x) if abs(x) < pi / 4.
 * 
 * The task is to calculate cos(x) if x in [- pi / 4; pi / 4]
 * with the precision of a specified epsilon (ep).
 * In other words, abs(s_n - s_(n - 1)) < ep.
 * 
 * Accomplish the goal using both the iterative and recursive approaches.
 */
import acm.program.ConsoleProgram;

public class Cos extends ConsoleProgram {
	private static final long serialVersionUID = 1L;

	public void run() {
		while (true) {
			// input: fail fast
			double x = readDouble("Enter x: ");
			if (Math.abs(x) > Math.PI / 4) {
				println("x must be in [-pi/4; pi/4]");
				continue;
			}
			double ep = readDouble("Enter ep: ");
			if (ep <= 0) {
				println("ep must be positive");
				continue;
			}

			println("The value of cos(x) (iterative): " + sumIterative(ep, x));
			println("The value of cos(x) (recursive): " + sumRecursive(ep, x, 1, 1));
			println("The value of cos(x) from Math: " + Math.cos(x));
		}
	}

	private double sumIterative(double ep, double x) {
		double sum = 0;
		double sum0 = 0;
		int n = 0;

		while (true) {
			sum0 = sum;
			sum += (Math.pow(-1, n) * Math.pow(x, 2 * n)) / factorial(2 * n);
			n++;
			if (ep > Math.abs(sum - sum0)) {
				// already precise enough
				break;
			}
		}

		return sum;
	}

	private double sumRecursive(double ep, double x, int n, double i) {
		if (ep > Math.abs(i * (-1) * x * x / (2 * n * (2 * n - 1)))) {
			// already precise enough
			return 1;
		}

		return i * (-1) * x * x / (2 * n * (2 * n - 1))
			+ sumRecursive(ep, x, n + 1, i * (-1) * x * x / (2 * n * (2 * n - 1)));
	}

	private long factorial(int n) {
		if (n == 0) {
			return 1;
		}
		return n * factorial(n - 1);
	}
}
