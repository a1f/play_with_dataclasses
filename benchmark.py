from dataclasses import dataclass
import time
from typing import NamedTuple
import sys

S = 0


@dataclass
class TestDC:
    a: int
    b: str

    def change(self):
        global S
        S += self.a


class TestNT(NamedTuple):
    a: int
    b: str

    def change(self):
        global S
        S += self.a

print("Benchmarking")

start_time = time.time()
all_dc = [TestDC(i, "a") for i in range(1000000)]
print("Creation for dataclass: %.5f sec" % (time.time() - start_time))

start_time = time.time()
all_nt = [TestNT(i, "a") for i in range(1000000)]
print("Creation for NamedTuples: %.5f sec" % (time.time() - start_time))

sum = 0
start_time = time.time()
for dc in all_dc:
    sum += dc.a
print("Access for dataclass: %.5f sec" % (time.time() - start_time))

sum = 0
start_time = time.time()
for nt in all_nt:
    sum += nt.a
print("Read for NamedTuples: %.5f sec" % (time.time() - start_time))


start_time = time.time()
for dc in all_dc:
    dc.change()
print("Method for dataclass: %.5f sec" % (time.time() - start_time))


start_time = time.time()
for nt in all_nt:
    nt.change()
print("Method for NamedTuples: %.5f sec" % (time.time() - start_time))

print("Size of dataclass: %.5f" % sys.getsizeof(all_dc[0]))
print("Size of NamedTuples: %.5f" % sys.getsizeof(all_nt[0]))
