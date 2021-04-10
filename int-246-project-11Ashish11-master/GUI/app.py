from flask import Flask , render_template, redirect, request, url_for, flash
import skfuzzy as fuzz
import numpy as np
from matplotlib import pyplot as plt


app = Flask(__name__)


@app.route('/results')
def correct(val1, val2, A  , B): #, B, C, D):
    return render_template("results.html", value1=val1, value2=val2 , A=A , B=B ) #, B=B, C=C, D=D)


@app.route('/')
def home():
    return render_template("index.html")



@app.route('/', methods=['POST'])
def index():
    
#    return "worked"
    
    windspeed = np.arange(0, 100, 1)
    numberofwindmills = np.arange(0, 100, 1)
    x_power = np.arange(0, 100, 1)


    lowwindspeed = fuzz.trimf(windspeed, [0, 15, 30])
    midwindspeed = fuzz.trimf(windspeed, [20, 50, 70])
    highwindspeed = fuzz.trimf(windspeed, [60, 85, 100])

    lowwindmills = fuzz.trimf(numberofwindmills, [0, 15, 30])
    midwindmills = fuzz.trimf(numberofwindmills, [20, 50, 70])
    highwindmills = fuzz.trimf(numberofwindmills, [60, 85, 100])

    power_lo = fuzz.trimf(x_power, [0, 20, 40])
    #power_med = fuzz.trimf(x_power, [10, 25, 40])
    power_md = fuzz.trimf(x_power, [20, 45, 65])
    #power_dec = fuzz.trimf(x_power, [45, 65, 75])
    power_hi = fuzz.trimf(x_power, [55 , 70 , 100])


    wind = int(request.form['input1'])
#    power.input['wind_speed'] = wind
    number = int(request.form['input2'])
#    power.input['noofwindmills'] = number



    
    windspeed_level_lo = fuzz.interp_membership(windspeed, lowwindspeed, wind)
    windspeed_level_md = fuzz.interp_membership(windspeed, midwindspeed, wind)
    windspeed_level_hi = fuzz.interp_membership(windspeed, highwindspeed, wind)

    numberofwindmills_level_lo = fuzz.interp_membership(numberofwindmills, lowwindmills, number)
    numberofwindmills_level_md = fuzz.interp_membership(numberofwindmills, midwindmills, number)
    numberofwindmills_level_hi = fuzz.interp_membership(numberofwindmills, highwindmills, number)



    # Now we take our rules and apply them. Rule 1 concerns bad food OR numberofwindmillsice.
    # The OR operator means we take the maximum of these two.
    active_rule1 = np.fmax(windspeed_level_lo, numberofwindmills_level_lo)


    # Now we apply this by clipping the top off the corresponding output
    # membership function with `np.fmin`
    power_activation_lo = np.fmin(active_rule1, power_lo) # removed entirely to 0

    # For rule 2 we connect acceptable numberofwindmillsice to medium power
    power_activation_md = np.fmin(numberofwindmills_level_md, power_md)

    # For rule 3 we connect high numberofwindmillsice OR high food with high power
    active_rule3 = np.fmax(windspeed_level_hi, numberofwindmills_level_hi)

    power_activation_hi = np.fmin(active_rule3, power_hi)

    power0 = np.zeros_like(x_power)


    # Visualize this
    fig, ax0 = plt.subplots(figsize=(8, 3))
    ax0.fill_between(x_power, power0, power_activation_lo, facecolor='b', alpha=0.7)
    ax0.plot(x_power, power_lo, 'b', linewidth=0.5, linestyle='--', )

    ax0.fill_between(x_power, power0, power_activation_md, facecolor='g', alpha=0.7)
    ax0.plot(x_power, power_md, 'g', linewidth=0.5, linestyle='--')

    ax0.fill_between(x_power, power0, power_activation_hi, facecolor='r', alpha=0.7)
    ax0.plot(x_power, power_hi, 'r', linewidth=0.5, linestyle='--')

    ax0.set_title('Output membership activity')


    # Turn off top/right axes
    for ax in (ax0,):
        ax.spines['top'].set_visible(False)
        ax.spines['right'].set_visible(False)
        ax.get_xaxis().tick_bottom()
        ax.get_yaxis().tick_left()
    plt.tight_layout()




    aggregated = np.fmax(power_activation_lo, np.fmax(power_activation_md, power_activation_hi))
    # Calculate defuzzified result
    power = fuzz.defuzz(x_power, aggregated, 'centroid')
    power_activation = fuzz.interp_membership(x_power, aggregated, power) # for plot
    # Visualize this
    fig, ax0 = plt.subplots(figsize=(8, 3))
    ax0.plot(x_power, power_lo, 'b', linewidth=0.5, linestyle='--', )
    ax0.plot(x_power, power_md, 'g', linewidth=0.5, linestyle='--')
    ax0.plot(x_power, power_hi, 'r', linewidth=0.5, linestyle='--')
    ax0.fill_between(x_power, power0, aggregated, facecolor='g', alpha=0.7)
    ax0.plot([power, power], [0, power_activation], 'k', linewidth=1.5, alpha=0.9)
    ax0.set_title('Aggregated membership and result (line)')
    # Turn off top/right axes

    for ax in (ax0,):
        ax.spines['top'].set_visible(False)
        ax.spines['right'].set_visible(False)
        ax.get_xaxis().tick_bottom()
        ax.get_yaxis().tick_left()
    plt.tight_layout()
    

    plt.savefig("static/temp2.jpg")
#    plt.savefig("temp2.jpg")
#    plt.savefig("static/images/temp2.jpg")
    
#    plt.savefig("static/temp2.jpg")



    #letstry = Power.view(sim=power)
    #print(letstry)

    return correct( wind , number , power , "/static/images/temp2.jpg" )
    #Power.view(sim=power)
    
    #End Of Fuzzy 
    
    
if __name__ == '__main__':
   app.debug = True
   app.run()