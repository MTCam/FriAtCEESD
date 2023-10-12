def kinetic_energy(self, cv: ConservedVars):
    return (0.5 * np.dot(cv.momentum, cv.momentum) / cv.mass)

def internal_energy(self, cv: ConservedVars):
    return (cv.energy - self.kinetic_energy(cv))

def pressure(self, cv: ConservedVars):
    return self.internal_energy(cv) * (self._gamma - 1.0)

