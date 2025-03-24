import json
import numpy as np

def interpolate_points(p1, p2, num_points):
    latitudes = np.linspace(p1[1], p2[1], num_points)
    longitudes = np.linspace(p1[0], p2[0], num_points)
    return list(zip(longitudes, latitudes))

def create_geojson_with_interpolated_points(target_vertices):
    coordinates = [
                        [-48.1622, -22.2156],
                        [-48.1403, -22.2004],
                        [-48.1183, -22.1853],
                        [-48.0963, -22.1702],
                        [-48.0744, -22.155],
                        [-48.0524, -22.1399],
                        [-48.0305, -22.1248],
                        [-48.0086, -22.1096],
                        [-47.9866, -22.0945],
                        [-47.9647, -22.0793],
                        [-47.9428, -22.0642],
                        [-47.9411, -22.0504],
                        [-47.9394, -22.0366],
                        [-47.9378, -22.0228],
                        [-47.9241, -22.0294],
                        [-47.9104, -22.0361],
                        [-47.8967, -22.0428],
                        [-47.9036, -22.0588],
                        [-47.9106, -22.0748],
                        [-47.9176, -22.0908],
                        [-47.9246, -22.1068],
                        [-47.9316, -22.1228],
                        [-47.9385, -22.1388],
                        [-47.9455, -22.1548],
                        [-47.9525, -22.1708],
                        [-47.9549, -22.1881],
                        [-47.9574, -22.2054],
                        [-47.9598, -22.2228],
                        [-47.9623, -22.2401],
                        [-47.9647, -22.2574],
                        [-47.9672, -22.2747],
                        [-47.9696, -22.292],
                        [-47.9721, -22.3093],
                        [-47.9745, -22.3266],
                        [-47.9769, -22.3439],
                        [-47.9955, -22.3311],
                        [-48.014, -22.3182],
                        [-48.0326, -22.3054],
                        [-48.0511, -22.2926],
                        [-48.0696, -22.2797],
                        [-48.0882, -22.2669],
                        [-48.1067, -22.2541],
                        [-48.1252, -22.2412],
                        [-48.1437, -22.2284],
                        [-48.1622, -22.2156]
                    ]
  
    total_existing_points = len(coordinates)
    points_needed = target_vertices - total_existing_points
  
    new_coordinates = []
  
    for i in range(total_existing_points - 1):
        p1 = coordinates[i]
        p2 = coordinates[i + 1]
      
        num_points = int(np.ceil(points_needed / (total_existing_points - 1)))  # Even distribution
        interpolated = interpolate_points(p1, p2, num_points)
        
        new_coordinates.extend(interpolated)
        points_needed -= (num_points - 1)  # Subtract the number of added points
    
    new_coordinates.append(coordinates[-1])
    coordinates = [new_coordinates]

    print(coordinates)

create_geojson_with_interpolated_points(10000)
