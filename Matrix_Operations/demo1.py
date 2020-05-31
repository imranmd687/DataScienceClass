import numpy as np
import scipy.linalg as la


def matrix_multiplication(a, b):
    return a.dot(b)


def matrix_inverse(a):
    return np.linalg.inv(a)


def matrix_eigenvalues(a):
    return la.eig(a)


def dotproduct_vectors(a, b):
    return np.vdot(a, b)


def matrix_determinant(a):
    return np.linalg.det(a)


def rotation_matrix(degree):
    theta = np.radians(degree)
    cos_theta, sin_theta = np.cos(theta), np.sin(theta)
    return np.array(((cos_theta, -sin_theta), (sin_theta, cos_theta)))


def rotate_matrix(a, degree):
    return np.dot(a, rotation_matrix(degree))


def matrix_diagonalize(A):
    eigvals, eigvecs = matrix_eigenvalues(A)
    eigvals = eigvals.real
    D = np.diag(eigvals)
    return eigvecs, D, matrix_inverse(eigvecs)


def matrix_power(A, n):
    eigvecs, eigvals, eigvecs_inv = matrix_diagonalize(A)
    eigvals_power = np.power(eigvals, n)
    return eigvecs @ eigvals_power @ matrix_inverse(eigvecs)


if __name__ == "__main__":
    a = np.array([[5, 1, 3], [1, 1, 1], [1, 2, 1]])
    print("a = ", a)
    a = a * 2
    print("Scalar multiplication")
    print("a*2 =", a)
    b = np.array([1, 2, 3])
    print("matrix inverse")
    print(matrix_inverse(a))
    print("matrix multiplication")
    print(matrix_multiplication(a, b))
    print(a * b)

    print("eigenvalues,eigen vectors")
    print(matrix_eigenvalues(a))

    c = np.array([[1, 2], [3, 4]])
    d = np.array([[11, 12], [13, 14]])
    print("dot product vectors")
    print(dotproduct_vectors(c, d))
    e = np.array([[6, 1, 1], [4, -2, 5], [2, 8, 7]])
    print("matrix determinent")
    print(matrix_determinant(e))
    print("rotational matrix")
    print(rotation_matrix(30))

    m = np.array([[1, 2], [3, 4], [5, 6]], int)
    print("matrix rotation 30 degree")
    print(m)
    print(rotate_matrix(m, 30))

    A = np.array([[1, 3], [6, -2]])
    print("matrix diagonalization")
    print(matrix_diagonalize(A))
    # print(matrix_diagonalize(A)[0] @ matrix_diagonalize(A)[1] @ matrix_diagonalize(A)[2])

    print("power of a matrix")
    print(matrix_power(A, 4))
