import math
import matplotlib.pyplot as plt

e = math.e


def dy(x, y):
    return y / (2 * math.sqrt(x))


def getPoints(N, a=0, b=1):
    h = (b - a) / N
    points = []
    cur_point = a
    for i in range(N+1):
        points.append(cur_point)
        cur_point += h
    return points, h


# Точное решение задачи Коши
def get_exact_solution(x):
    return 2 * math.pow(e, math.sqrt(x))  # y= 2e^(sqrt(x))


# Явный метод Эйлера
def get_euler_solution(points, h):
    result = [2]  # y(0)=2
    cur_y = 2  # y(0)=2
    for x in points[1:]:
        cur_y = cur_y + dy(x, cur_y) * h
        result.append(cur_y)

    return result


# метод Коши
def get_cauchy_solution(points, h):
    result = [2]  # y(0)=2
    cur_y = 2  # y(0)=2

    for x in points[1:]:
        half_y = cur_y + (h / 2) * dy(x, cur_y)
        cur_y = cur_y + h * dy(x + (h / 2), half_y)
        result.append(cur_y)

    return result


# Метод Адамса-Мултона (Неявный метод Адамса 3-го порядка)
def get_adams_solution(points, h):
    result = [2]  # y(0)=2
    cur_y = 2  # y(0)=2
    for x in points[1:]:
        cur_y = \
            (2 * math.sqrt(x + h) * (2 * cur_y + h * dy(x, cur_y))) / (
                        4 * math.sqrt(x + h) - h) # вывод в доке

        result.append(cur_y)

    return result


def main():
    get_result(10)
    get_result(20)
    get_result(30)
    get_result(1500)


def get_result(N):
    print()
    points, h = getPoints(N)
    print("N = " + str(N))
    print("h = ", h)
    print("точки", points)

    euler_solution = get_euler_solution(points, h)
    print("метод Эйлера", euler_solution)

    cauchy_solution = get_cauchy_solution(points, h)
    print("метод Коши", cauchy_solution)

    adams_solution = get_adams_solution(points, h)
    print("метод Адамса-Мултона", adams_solution)

    exact_solution = list(map(lambda x: get_exact_solution(x), points))
    print("Точное решение", exact_solution)

    plt.plot(points, euler_solution,)
    plt.plot(points, cauchy_solution)
    plt.plot(points, adams_solution)
    plt.plot(points, exact_solution)
    plt.legend(["метод Эйлера","метод Коши","метод Адамса-Мултона","Точное решение"])
    plt.show()


if __name__ == '__main__':
    main()
