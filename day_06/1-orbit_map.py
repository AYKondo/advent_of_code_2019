class OrbitsList:
    def __init__(self):
        self.orbits = {}
    
    def link_orbits(self, orbit_name, orbit_around):
        if self.check_orbit(orbit_name):
            orbit_1 = self.orbits[orbit_name]
        else:
            orbit_1 = self.add_orbit(orbit_name)

        if self.check_orbit(orbit_around):
            orbit_2 = self.orbits[orbit_around]
        else:
            orbit_2 = self.add_orbit(orbit_around)
        
        orbit_1.around = orbit_2
    
    def check_orbit(self, orbit_name):
        if orbit_name in self.orbits:
            return True
        return False
    
    def add_orbit(self, orbit_name):
        self.orbits[orbit_name] = Orbit(orbit_name)
        return self.orbits[orbit_name]
    
    def count_direct_indirect_orbits(self):
        total_count = 0
        orbit_map = {}
        for orbit in self.orbits:
            current_orbit = self.orbits[orbit]
            # Calculate the orbits, if the orbit already calculated, break and use the map
            count = self.calculate_distance(orbit_map, current_orbit)

            total_count += count
            orbit_map[orbit] = count

        return total_count

    def calculate_distance(self, orbit_map, orbit):
        count = 0
        while orbit.around != None:
            if orbit.name in orbit_map:
                count += orbit_map[orbit.name]
                break
            else:
                count += 1

            orbit = orbit.around
        return count

class Orbit:
    def __init__(self, name):
        self.name = name
        self.around = None

if __name__ == "__main__":
    orbits = OrbitsList()
    with open('day_06/input.txt', 'r') as f:
        for line in f:
            line_orbits = line.replace('\n', '').split(")")
            orbit_1 = line_orbits[0]
            orbit_2 = line_orbits[1]
            orbits.link_orbits(orbit_2, orbit_1)

        print(orbits.count_direct_indirect_orbits())
        