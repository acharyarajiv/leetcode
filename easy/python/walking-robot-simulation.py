'''
steps
    1. convert 2d obstacle array to 1d set for easier and faster lookup
    2. define directions with respsect to a 2d matrix board
        north = [0, 1] i.e stay on same column and move a row up
        east = [0, 1] i.e stay on same row and column in front
        south = [0, -1] i.e stay on same column and move a  row in down
        west = [-1, 0] i.e stay on same row and move a column in back
    3. direction_index indicate where would robot move next
    4. update direction_index when command == -1 or -2
    5. move one step at time as long as obstacle is not hit
    6. calculate eucladian distance and return the square of the maximum Euclidean distance that the robot will be from the origin
'''


class Solution(object):
    def buildSingleDimensionGrid(self, obstacles):
        obs_grid = set([])
        for grid in obstacles:
            obs_grid.add(str(grid[0]) + '-' + str(grid[1]))
        return obs_grid

    def robotSim(self, commands, obstacles):
        """
        :type commands: List[int]
        :type obstacles: List[List[int]]
        :rtype: int
        """
        obs_grid = self.buildSingleDimensionGrid(obstacles)
        directions = [
                        [0, 1],
                        [1, 0],
                        [0, -1],
                        [-1, 0]
                     ]
        direction_index, x_axis, y_axis, res = 0, 0, 0, 0
        for command in commands:
            if command == -1:
                direction_index += 1
                if direction_index > 3:
                    direction_index = 0
            elif command == -2:
                direction_index -= 1
                if direction_index < 0:
                    direction_index = 3
            else:
                while command > 0 and str(x_axis + directions[direction_index][0]) + '-' + str(y_axis + directions[direction_index][1]) not in obs_grid:
                    x_axis += directions[direction_index][0]
                    y_axis += directions[direction_index][1]
                    command -= 1
            res = max(res, x_axis * x_axis + y_axis * y_axis)
        return res


if __name__ == '__main__':
    inp_arr = [
                [[4, -1, 3], []],
                [[4, -1, 4, -2, 4], [[2, 4]]]
              ]
    out_arr = [25, 65]
    s = Solution()
    for i, inp in enumerate(inp_arr):
        res = s.robotSim(inp[0], inp[1])
        print('input commands %s obstacles %s' % (inp[0], inp[1]))
        print('output actual %d expected %d\n' % (res, out_arr[i]))
