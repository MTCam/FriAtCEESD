def pressure(self, cv: ConservedVars):
    temperature = self.temperature(cv)
    y = self.mass_fractions(cv)
    return self._prometheus_mech.get_pressure(cv.mass,
                                              temperature,
                                              y)

def temperature(self, cv: ConservedVars):
    y = self.mass_fractions(cv)
    e = self.internal_energy(cv) / cv.mass
    tguess = 300.0
    return self._prometheus_mech.get_temperature(e,
                                                 tguess,
                                                 y, True)
