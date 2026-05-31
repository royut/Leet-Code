class Solution(object):
    def asteroidsDestroyed(self, mass, asteroids):
        """
        :type mass: int
        :type asteroids: List[int]
        :rtype: bool
        """
        asteroids.sort()
        print(asteroids)
        for ass in asteroids:
            if mass > ass:
                mass += ass
        return mass >= asteroids[-1]


if __name__ == "__main__":
    print('in main')
    mass = 10
    asteroids = [3, 9, 19, 5, 21]
    print(Solution().asteroidsDestroyed(mass, asteroids))