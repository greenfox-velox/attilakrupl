class MapData:
    
    def __init__(self):
        
        self.game_map = [[0,0,0,1,0,1,0,0,0,0],
                        [0,0,0,1,0,1,0,1,1,0],
                        [0,1,1,1,0,1,0,1,1,0],
                        [0,0,0,0,0,1,0,0,0,0],
                        [1,1,1,1,0,1,1,1,1,0],
                        [0,1,0,1,0,0,0,0,1,0],
                        [0,1,0,1,0,1,1,0,1,0],
                        [0,0,0,0,0,1,1,0,1,0],
                        [0,1,1,1,0,0,0,0,1,0],
                        [0,0,0,1,0,1,1,0,1,0],
                        [0,1,0,1,0,1,0,0,0,0]] 
        
    def generate_coordinate_list(self):
        map_coordinates = []
        for i in range(len(self.game_map)):
            for j in range(len(self.game_map[i])):
                if self.game_map[i][j] == 0:
                    map_coordinates.append({"x":i, "y": j, "t":0})
                else:
                    map_coordinates.append({"x":i, "y": j, "t":1})
        return map_coordinates
    
    


                    
                    
        
        