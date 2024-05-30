import numpy as np
import unittest

def jacobi_matrix_iteration(A, b, x0, tol, max_iter):
    n = len(b)
    x = x0
    D = np.diag(np.diag(A))
    R = A - D
    if not check_spectral_radius_less_than_1(D, R):
        raise ValueError("Spectral radius is not less than 1, Jacobi method may not converge.")

    for i in range(max_iter):
        x_new = np.linalg.solve(D, b - np.dot(R, x))
        if np.linalg.norm(x_new - x) < tol:
            return x_new
        x = x_new
    return x

def check_spectral_radius_less_than_1(D, R):
    M = np.dot(np.linalg.inv(D), R)
    return np.max(np.abs(np.linalg.eigvals(M))) < 1


class TestJacobi(unittest.TestCase):

    def test_jacobi_small(self):
        A = np.array([[8, 5, 2], [2, 10, -2], [1, 3, 6]])
        b = np.array([25, 20, 30])
        x0 = np.array([0, 0, 0])
        tol = 1e-10
        max_iter = 100

        actual = jacobi_matrix_iteration(A, b, x0, tol, max_iter)
        expected = np.linalg.solve(A, b) # which is [0.6, 2.6, 3.6]

        self.assertTrue(np.allclose(actual, expected, atol=1e-10, rtol=1e-10))

if __name__ == '__main__':
    unittest.main()


