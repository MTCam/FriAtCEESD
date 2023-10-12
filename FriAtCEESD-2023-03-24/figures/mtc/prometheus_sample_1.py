def get_density(self, pressure,
                temperature, massfractions):
    return self._prometheus_mech.get_density(pressure,
                                             temperature,
                                             massfractions)

def get_species_molecular_weights(self):
    return self._prometheus_mech.wts

def get_production_rates(self, cv: ConservedVars):
    return (
        self._prometheus_mech.get_net_production_rates(cv.mass,
                    self.temperature(cv),cv.massfractions)
