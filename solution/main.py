from solution.wedding_algorithm import WeddingAlgorithm

file_template = '../test_files/in/'


def main(file):
    """
    main function to run algorithm
    :param file: input file with data
    :return:
    >>> main(file_template + 'data1.in')
    6
    >>> main(file_template + 'data2.in')
    24
    >>> main(file_template + 'data3.in')
    6

    """
    wedding = WeddingAlgorithm(file)
    result = wedding.find_pairs_amount()
    return result


if __name__ == '__main__':
    import doctest

    doctest.testmod(verbose=True)
