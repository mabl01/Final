from functions import *

def physics_helper():
    print "Hello! Welcome to the Physics Number Hub!\nWhat category are you looking for help in?\nNote: Meters, Seconds, Meters/Sec, Meters/Sec^2, and Radians are expected units"
    category = raw_input("Reference, Mechanics, E/M, Data, or Misc?: ")

    if category == "mechanics" or category == "Mechanics":
        print "\nHere are the currently supported equations for mechanical physics:\nPosition (pos), Velocity (v), Centripetal Force (cf), Momentum (mntm), Kinetic Energy (ek), Work Performed on a System (work), and Gravitational Force (grav)"
        equation = raw_input("Which equation do you need? (use the abbreviation, eg pos for Position): ")
        
        if equation == "pos":
            initpos = raw_input("Enter initial position: ")
            initv = raw_input("Enter the initial velocity: ")
            time = raw_input("Enter the time elapsed: ")
            accel = raw_input("Enter the acceleration: ")
            return position(float(initpos), float(initv), float(time), float(accel))
        
        elif equation == "v":
            initv = raw_input("Enter the initial velocity: ")
            accel = raw_input("Enter the acceleration: ")
            time = raw_input("Enter the time elapsed: ")
            return velocity(float(initv), float(accel), float(time))

        elif equation == 'cf':
            velo = raw_input("Enter the velocity: ")
            radius = raw_input("Enter the radius: ")
            return centripetal(float(velo), float(radius))

        elif equation == 'mntm':
            mass = raw_input("Enter the mass: ")
            velocity = raw_input("Enter the velocity: ")
            return momentum(float(mass), float(velocity))

        elif equation == 'ek':
            mass = raw_input("Enter the mass: ")
            velocity = raw_input("Enter the velocity: ")
            return kinetic(float(mass), float(velocity))

        elif equation == 'work':
            force = raw_input("Enter the force used: ")
            distance = raw_input("Enter the distance moved: ")
            angle = raw_input("Enter the angle of force (0 rads if parallel with surface): ")
            return work(float(force), float(distance), float(angle))
        
        else:
            return "Sorry, that is not a recognized formula. Please try again."
            
    elif category == "E/M" or category == "e/m":
        print "\nHere are the currently supported equations for electricity and magnetism:\nElectric Potential (epot), Current (i), Power (p), Electric Field Strength (efs), Potential Energy (eg), and EMF (emf)"
        equation = raw_input("Which equation do you need? (use the abbreviation, eg epot for Electric Potential): ")

        if equation == "epot":
            charge = raw_input("Enter the charge: ")
            capacitance = raw_input("Enter the capacitance: ")
            return epot(float(charge), float(capacitance))

        elif equation == 'i':
            charge = raw_input("Enter the charge: ")
            time = raw_input("Enter the time elapsed: ")
            return current(float(charge), float(time))

        elif equation == 'p':
            current = raw_input("Enter the current: ")
            epot = raw_input("Enter the electric potential: ")
            return power(float(current), float(epot))

        elif equation == 'efs':
            epot = raw_input("Enter the electric potential: ")
            radius = raw_input("Enter the radius: ")
            return field(float(epot), float(radius))

        elif equation == 'eg':
            charge = raw_input("Enter the charge: ")
            epot = raw_input("Enter the electroic potential: ")
            return potential(float(charge), float(epot))

        elif equation == 'emf':
            ms = raw_input("Enter the magnetic field strength: ")
            length = raw_input("Enter the length of object: ")
            speed = raw_input("Enter the speed of object: ")
            return emf(float(ms), float(length), float(speed))

        else:
            return "Sorry, that is not a recognized formula. Please try again."

    elif category == "Data" or category == 'data':
        print "\nHere are the available data-sorting methods:\nMean (avg) and Range (rng)"
        equation = raw_input("Which function do you need? (use the abbreviation, eg avg for Mean): ")
        
        if equation == "avg":
            user_list = raw_input("Enter your list of numbers: ")
            param = raw_input("Enter what your list is split by (e.g. for 1,2,3 it would be ,): ")
            return avg(user_list, param)

        elif equation == 'rng':
            user_list = raw_input("Enter your list of numbers: ")
            param = raw_input("Enter what your list is split by (e.g. for 1,2,3 it would be ,): ")
            return datarange(user_list, param)

        else:
            return "Sorry, that is not a recognized formula. Please try again."

    elif category == "Misc" or category == "misc":
        print "\nHere are the other miscellaneous functions including fluid dynamics and modern physics:\nPressure (ps), Einstein's Energy (e), and Wavelength (wl)"
        equation = raw_input("Which function do you need? (use the abbreviation, eg ps for Pressure): ")
        
        if equation == "ps":
            force = raw_input("\nEnter the force: ")
            area = raw_input("Enter the area: ")
            return press(float(force), float(area))

        elif equation == "e":
            mass = raw_input("\nEnter the mass: ")
            return einstein(float(mass))

        elif equation == 'wl':
            freq = raw_input("\nEnter the frequency: ")
            velocity = raw_input("Enter the wave speed: ")
            return wl(float(velocity), float(freq))

        else:
            return "Sorry, that is not a recognized formula. Please try again."

    elif category == "reference" or category == "Reference":
        ## VALUES
        proton = '1.67e-27 kg'
        neutron = proton
        electron = '9.11e-31 kg'
        echarge = '1.6e-19 C'
        r = '8.31 J/(mol*K)'
        gc = '6.67e-11 m^3/(kg*s^2)'
        sol = '2.9e8 m/s'
        ev = '1.6e-19 J'
        acc_earthgrav = '9.8 m/s^2'
        plancks = '6.63e-34 J*s'
        print "\nThese are the constant values:\nProton/Neutron Mass (pnm), Electron Mass (em), Electron Charge (ec), Electron Volt (ev), Univ. Gas Constant (r), Speed of Light (sol), Gravitational Constant (g), Acceleration due to Earth's Gravity (aeg), and Planck's Constant (pc)"
        choice = raw_input("\nWhich one do you need? (use the abbreviation like pnm for Proton/Neutron Mass): ")

        if choice == 'pnm':
            return proton

        elif choice == 'em':
            return electron

        elif choice == 'ec':
            return echarge

        elif choice == 'r':
            return r

        elif choice == 'g':
            return gc
        
        elif choice == 'sol':
            return sol

        elif choice == 'ev':
            return ev

        elif choice == 'aeg':
            return acc_earthgrav

        elif choice == 'pc':
            return plancks

        else:
            return "Sorry, that is not a recognized constant. Please try again."

    else:
        return "Sorry, that is not a recognized option. Please try again."

print physics_helper()
