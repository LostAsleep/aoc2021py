from utilities import read_file

"""
Surely, each lanternfish creates a new lanternfish once every 7 days.

However, this process isn't necessarily synchronized between every lanternfish
- one lanternfish might have 2 days left until it creates another lanternfish,
while another might have 4. So, you can model each fish as a single number 
that represents the number of days until it creates a new lanternfish.

Furthermore, you reason, a new lanternfish would surely need slightly longer 
before it's capable of producing more lanternfish: 
two more days for its first cycle.

So, suppose you have a lanternfish with an internal timer value of 3:

After one day, its internal timer would become 2.
After another day, its internal timer would become 1.
After another day, its internal timer would become 0.
After another day, its internal timer would reset to 6, and
it would create a new lanternfish with an internal timer of 8.
After another day, the first lanternfish would have an internal timer of 5, 
and the second lanternfish would have an internal timer of 7.

"""

INPT = "input_d06.txt"
DAYS1 = 80
DAYS2 = 256


class SchoolOfLanternfishes:

    def __init__(self, start_fishes):
        start_input = [int(x) for x in start_fishes[0].split(",")]
        self.pop = self.get_init_population(start_input)

    def get_init_population(self, start_input):
        init_pop = dict()
        for fish in start_input:
            init_pop[fish] = init_pop.get(fish, 0) + 1
        return init_pop

    def pass_day(self):
        temp_fishes = dict()
        for key, value in self.pop.items():
            if key == 0:
                temp_fishes[8] = temp_fishes.get(8, 0) + value
                temp_fishes[6] = temp_fishes.get(6, 0) + value
                continue
            temp_fishes[key-1] = temp_fishes.get(key-1, 0) + value
        self.pop = dict(temp_fishes)


puzzle_input = read_file(INPT)
print(puzzle_input)

lantern_fishes = SchoolOfLanternfishes(puzzle_input)
for _ in range(DAYS2):
    lantern_fishes.pass_day()

num_f = sum([x for x in lantern_fishes.pop.values()])
print(num_f)
