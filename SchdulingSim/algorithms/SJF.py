from queue import Queue
from algorithms import BaseSch
from worker import Worker
from time import sleep


class SPF(BaseSch):
    def pick_next(self):
        if self.i is None and self.w is None:
            w, i = self.q.popleft()
            return w, i
        elif self.burstArray[self.i] > 0:
            return self.w, self.i
        else:
            w, i = self.q.popleft()
            return w, i

    def init_queue(self):
        a = [(self.burstArray[i], i) for i in range(len(self.arrivalArray))]
        a.sort(key=lambda x: x[0])
        for i in range(len(self.burstArray)):
            self.q.append(self.processArray[a[i][1]])


if __name__ == '__main__':
    f = SPF([0, 1, 2, 3, 3], [8, 1, 4, 6, 2])
    f.run()
    print('wait',f.waitArray)
    print('com',f.comArray)
    print('burst',f.burstArray)
    for i in f.raw:
        print(i)
