def temperature(self, cv: ConservedVars):
    return (
        (((self._gamma - 1.0) / self._gas_const)
         * self.internal_energy(cv) / cv.mass)
    )

def sound_speed(self, cv: ConservedVars):
    actx = cv.mass.array_context
    return actx.np.sqrt(self._gamma * self.pressure(cv) / cv.mass)

def total_energy(self, cv, pressure):
    return (pressure / (self._gamma - 1.0)
            + self.kinetic_energy(cv))
