class WeddingAlgorithm:
    def __init__(self, file_in):
        """
        constructor for WeddingAlgorithm class where we initialize empty tribes dict, counter for tribes
        and lists filled with zeros for counting genders by tribe
        :param file_in: input file with all data to read
        """
        self.file_in = file_in
        with open(self.file_in, 'r') as input_data:
            self.connections_number = int(input_data.readline().rstrip())
            self.boys_counter_list = [0] * self.connections_number
            self.girls_counter_list = [0] * self.connections_number
            self.tribes = {}
            self.tribes_counter = 0
            self.iterations = 0

    def find_pairs_amount(self):
        """
        main function to find all possible pairs
        :return: amount of all possible pairs
        """
        connections = self.get_connections()
        for connection in connections:
            first_person = int(connection[0])
            second_person = int(connection[1])

            first_person_tribe = self.find_tribe_by_person(first_person)
            second_person_tribe = self.find_tribe_by_person(second_person)

            if first_person == second_person:
                if first_person_tribe is None:
                    self.create_tribe([first_person])
                continue
            if first_person_tribe is None and second_person_tribe is None:
                self.create_tribe([first_person, second_person])
            elif first_person_tribe is not None and second_person_tribe is None:
                self.add_new_person_to_existing_tribe(second_person, first_person_tribe)
            elif first_person_tribe is None and second_person_tribe is not None:
                self.add_new_person_to_existing_tribe(first_person, second_person_tribe)
            elif first_person_tribe is not None and second_person_tribe is not None:
                self.union_two_subtribes(first_person_tribe, second_person_tribe)
        answer = self.get_amount_of_possible_pairs()
        self.write_answer_to_file(answer)
        return answer

    def get_connections(self):
        """
        get connections from input file
        :return: list of binary lists with connections
        >>> wedding_test = WeddingAlgorithm('../test_files/in/data1.in')
        >>> wedding_test.get_connections()
        [['1', '2'], ['2', '4'], ['5', '8'], ['8', '9'], ['9', '10']]
        """
        with open(self.file_in, 'r') as input_data:
            next(input_data)
            return [line.split() for line in input_data]

    def find_tribe_by_person(self, person):
        """
        finds person`s tribe
        :param person: person to check tribe for
        :return: tribe if it exists for person, else None
        >>> wedding_test = WeddingAlgorithm('../test_files/in/data1.in')
        >>> wedding_test.tribes = {1: {1 , 3}, 2: {4, 6}}
        >>> wedding_test.find_tribe_by_person(3)
        1
        """
        for tribe_members in list(self.tribes.values()):
            if person in tribe_members:
                return list(self.tribes.keys())[list(self.tribes.values()).index(tribe_members)]

    def create_tribe(self, persons: list):
        """
        creates new tribe
        :param persons: list of two persons to add in new tribe
        :return:
        >>> wedding_test = WeddingAlgorithm('../test_files/in/data1.in')
        >>> wedding_test.create_tribe([1, 2])
        >>> wedding_test.tribes
        {1: {1, 2}}
        """
        self.tribes_counter += 1
        self.tribes[self.tribes_counter] = set()
        for person in persons:
            self.tribes[self.tribes_counter].add(person)
            self.check_gender(person, self.tribes_counter)

    def add_new_person_to_existing_tribe(self, new_person, existing_tribe):
        """
        adds new person to already existing tribe
        :param new_person: person to add
        :param existing_tribe: tribe to add in
        :return:
        """
        self.tribes[existing_tribe].add(new_person)
        self.check_gender(new_person, existing_tribe)

    def check_gender(self, person, tribe):
        """
        checks persons gender and increments it`s tribe`s gender counter
        :param person: person to check
        :param tribe: tribe to increment counter in
        :return:
        >>> wedding_test = WeddingAlgorithm('../test_files/in/data1.in')
        >>> wedding_test.tribes = {1: {1 , 3}, 2: {4, 6}}
        >>> wedding_test.check_gender(1, 1)
        >>> wedding_test.girls_counter_list[0]
        0
        """
        if person % 2 == 1:
            self.boys_counter_list[tribe - 1] += 1
        elif person % 2 == 0:
            self.girls_counter_list[tribe - 1] += 1

    def union_two_subtribes(self, first_subtribe, second_subtribe):
        """
        unions two 'subtribes' in one
        :param first_subtribe: one of tribes to union
        :param second_subtribe: one of tribes to union
        :return:
        """
        if len(self.tribes[first_subtribe]) > len(self.tribes[second_subtribe]):
            tribe_to_extend = first_subtribe
            tribe_to_remove = second_subtribe
        else:
            tribe_to_extend = second_subtribe
            tribe_to_remove = first_subtribe

        self.tribes[tribe_to_extend] += self.tribes.pop(tribe_to_remove)

        self.boys_counter_list[tribe_to_extend - 1] += self.boys_counter_list.pop(tribe_to_remove - 1)
        self.girls_counter_list[tribe_to_extend - 1] += self.girls_counter_list.pop(tribe_to_remove - 1)

    def get_amount_of_possible_pairs(self):
        """
        calculates amount of all possible pairs
        :return: amount of all possible pairs
        >>> wedding_test = WeddingAlgorithm('../test_files/in/data1.in')
        >>> wedding_test.tribes = {1: {1 , 3}, 2: {4, 6}}
        >>> wedding_test.boys_counter_list = [1, 2]
        >>> wedding_test.girls_counter_list = [2, 1]
        >>> wedding_test.get_amount_of_possible_pairs()
        5
        """
        duplicates = boys_counter = girls_counter = 0
        for iterator in range(0, len(list(self.tribes.keys()))):
            boys_counter += self.boys_counter_list[iterator]
            girls_counter += self.girls_counter_list[iterator]
            duplicates += self.boys_counter_list[iterator] * self.girls_counter_list[iterator]
        return boys_counter * girls_counter - duplicates

    def write_answer_to_file(self, answer):
        """
        writes answer into new file in 'test_files/out'
        :param answer: answer to write in file
        :return:
        """
        with open('../test_files/out/' + self.file_in.split('/')[-1][:-3] + '.out', 'w') as output_file:
            output_file.write(str(answer))


if __name__ == '__main__':
    import doctest

    doctest.testmod(verbose=True)
