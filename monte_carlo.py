import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import quad

# Функція
def f(x):
    return x**2 + 6*x + 5

def monte_carlo(a, b, num_samples, ax=None):

    # Генерування випадкових точок
    x_rand = np.random.uniform(a, b, N)
    y_rand = np.random.uniform(0, f_max, num_samples)
    under_curve = y_rand < f(x_rand)

    # Оцінка площі
    area_under_curve = (b - a) * f_max * np.sum(under_curve) / N

    # Візуалізація
    x = np.linspace(a, b, 500)
    y = f(x)
    ax = ax if ax else plt.gca()
    ax.plot(x, y, 'r-', label='f(x) = x² + 6x + 5')
    ax.fill_between(x, y, alpha=0.2, color='gray', label='Аналітична площа')
    ax.scatter(x_rand[under_curve], y_rand[under_curve], color='green', s=1, label='Під кривою')
    ax.scatter(x_rand[~under_curve], y_rand[~under_curve], color='blue', s=1, label='Над кривою')
    ax.set_title(f'N = {N}\nОцінка: {area_under_curve:.4f}, Аналітична: {true_area:.4f}')
    ax.set_xlabel('x')
    ax.set_ylabel('f(x)')
    ax.legend()
    ax.grid(True)

    return area_under_curve

if __name__ == "__main__":

    # Межі інтегрування
    a, b = 0, 2
    f_max = f(b)
    true_area, _ = quad(f, a, b)  # Аналітичне значення
    print(f"Площа обчислена функцією quad: {true_area:.5f}")

    sample_sizes = [100, 1000, 10000, 100000]
    fig, axes = plt.subplots(2, 2, figsize=(14, 10))
    axes = axes.flatten()

    for i, N in enumerate(sample_sizes):
        # Оцінка площі
        area_estimate = monte_carlo(a, b, N, ax=axes[i])
        print(f"N={N}, Оцінка площі: {area_estimate:.5}")

    plt.suptitle('Метод Монте-Карло (геометричний): порівняння для різних N', fontsize=16)
    plt.tight_layout(rect=[0, 0, 1, 0.96])
    plt.show()