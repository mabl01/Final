sol = '2.9e8'

# MECHANICS

def velocity(initial, acceleration, time):
    final_velocity = initial + (acceleration * time)
    return "Using the formula Vf = Vo + (a*t): The final velocity is ", final_velocity, " meters per second."

def position(initial, init_velocity, time, acceleration):
    final_position = initial + (init_velocity * time) + ((acceleration * time * time)/2)
    return "Using the formula Xf = Xo + (Vo*t) + (a*t^2)/2: The final position is " + str(final_position) + " meters."

def centripetal(velocity, radius):
    centripetal_force = (velocity * velocity) / radius
    return "Using the formula (V^2)/r: The centripetal force is " + str(centripetal_force) + " newtons."

def momentum(mass, velocity):
    momentum_value = mass * velocity
    return "Using the formula m*v: The momentum of the object is " + str(momentum_value) + "kilogram meters per second."

def kinetic(mass, velocity):
    kinetic_energy = ((mass * velocity * velocity)/2)
    return "Using the forula Ek = (m*v^2)/2: The kinetic energy is " + str(kinetic_energy) + " joules."

def work(force, distance, angle):
    import math
    worked = force * distance * math.cos(angle)
    return "Using the formula W = F * d * cos(a): The work performed on the system is " + str(worked) + " joules."

# E&M

def epot(charge, capacitance):
    elec_potential = charge / capacitance
    return "Using the formula charge/cap: The electric potential is " + str(elec_potential) + " volts."

def current(charge, time):
    amps = charge / time
    return "Using the formula charge/t: The current is " + str(amps) + " amps."

def power(current, epot):
    e_pow = current * epot
    return "Using the formula I * V: The power is " + str(e_pow) + " watts."

def field(epot, radius):
    field_strength = epot / radius
    return "Using the formula V / r: The field strength is " + str(field_strength) + " volts per meter."

def potential(charge, epot):
    pot_energy = (charge * epot) / 2
    return "Using the formula (charge*V) / 2: The potential energy is " + str(pot_energy) + " joules."

def emf(magnetic_strength, length, speed):
    emf_val = magnetic_strength * length * speed
    return "Using the formula B*l*V: The EMF is " + str(emf_val) + " volts."

# DATA COLLECTION

def datarange(user_list, param):
    numbers = user_list.split(str(param))
    min_val = numbers[0]
    max_val = numbers[0]
    for i in range(len(numbers)):
        if numbers[i] < min_val:
            min_val = numbers[i]
        elif numbers[i] > max_val:
            max_val = numbers[i]

    return "Subtracting the smallest number from the largest number: The range is " + str(float(max_val) - float(min_val))

def avg(user_list, param):
    numbers = user_list.split(str(param))
    sum = 0
    for i in range(len(numbers)):
        sum += float(numbers[i])
    return "Adding all the terms and dividing them by the amount of terms: The average is " + str(sum / len(numbers))

# MISC

def wl(velocity, freq):
    wavelength = velocity / freq
    return "Using the formula wl = v/freq: The wavelength is " + str(wavelength) + " meters."

def einstein(mass):
    e = mass * (float(sol) ** 2)
    return "Using the formula e = mc^2: The energy is " + str(e) + " joules."

def press(force, area):
    pressure = force / area
    return "Using the formula P = F/A: The pressure is " + str(pressure) + " pascals."
