from opentrons import protocol_api

metadata = {
    'apiLevel': '2.13',
    'protocolname': 'Streptavidin Affinity Purification',
    'description': '''Protocol for steps 24-33 of Protein extraction and quantification + affinity purification as listed in Benchling 2023-01-24''',
    'author': 'Jacob Cogan'
    }

def run(protocol: protocol_api.ProtocolContext):
    #defining instruments
    mag = protocol.load_module('magnetic module gen2', 10)
    tip200 = protocol.load_labware('opentrons_96_filtertiprack_200ul', 9)
    p300 = protocol.load_instrument('p300_multi_gen2', 'left', tip_racks=[tip200])
    reservoir = protocol.load_labware('usascientific_12_reservoir_22ml', 3)
    sample_plate = protocol.load_labware('biorad_96_wellplate_200ul_pcr', 4)
    finalsample_plate = protocol.load_labware('biorad_96_wellplate_200ul_pcr', 5)
    flowthrough_plate = protocol.load_labware('biorad_96_wellplate_200ul_pcr', 6)
    #defining flow rates
    p300.flow_rate.aspirate = 30 
    p300.flow_rate.dispense = 100
    p300.flow_rate.blow_out = 150

    #step 24
    #as of now, prep beads beforehand

    #step 25
    p300.pick_up_tip(tip200['A1'])
    count = 0

    while count < 1800:
        p300.mix(1, 50, sample_plate['A1'].bottom(z=0.5))
        protocol.delay(minutes=0.0167)
        count = count + 1

    p300.drop_tip()

    #step 26
    protocol.delay(minutes=1)
    mag.engage(height_from_base=7.5)
    protocol.delay(minutes=5)
    mag.disengage()

    #step 27
    p300.pick_up_tip(tip200['A2'])
    p300.aspirate(70, sample_plate['A1'].bottom(z=0.5))
    p300.dispense(70, flowthrough_plate['A1'])
    p300.drop_tip()

    #step 28
    protocol.delay(minutes=5)
    #mix 2.5ml 8M urea w/ 7.5ml 20mM EPPS so get 2M urea, work fast to preserve urea purity
    #place into resevoir X

    #step 29+30
    #wash buffer 1
    p300.pick_up_tip(tip200['A3'])
    p300.aspirate(125, reservoir['A1'])
    p300.dispense(125, sample_plate['A1'])
    p300.aspirate(125, reservoir['A1'])
    p300.dispense(125, sample_plate['A1'])
    count = 0

    while count < 60:
        p300.mix(1, 50, sample_plate['A1'].bottom(z=0.5))
        protocol.delay(minutes=0.0167)
        count = count + 1

    protocol.delay(minutes=1)
    mag.engage(height_from_base=7.5)
    protocol.delay(minutes=5)
    mag.disengage()

    protocol.delay(minutes=2)
    p300.aspirate(125, sample_plate['A1'].bottom(z=0.5))
    p300.dispense(125, reservoir['A6'])
    p300.aspirate(120, sample_plate['A1'].bottom(z=0.5))
    p300.dispense(120, reservoir['A6'])

    p300.drop_tip()

    #wash buffer 2
    p300.pick_up_tip(tip200['A4'])
    p300.aspirate(125, reservoir['A1'])
    p300.dispense(125, sample_plate['A1'])
    p300.aspirate(125, reservoir['A1'])
    p300.dispense(125, sample_plate['A1'])
    count = 0

    while count < 60:
        p300.mix(1, 50, sample_plate['A1'].bottom(z=0.5))
        protocol.delay(minutes=0.0167)
        count = count + 1

    protocol.delay(minutes=1)
    mag.engage(height_from_base=7.5)
    protocol.delay(minutes=5)
    mag.disengage()

    protocol.delay(minutes=2)
    p300.aspirate(125, sample_plate['A1'].bottom(z=0.5))
    p300.dispense(125, reservoir['A6'])
    p300.aspirate(120, sample_plate['A1'].bottom(z=0.5))
    p300.dispense(120, reservoir['A6'])

    p300.drop_tip()

    #sodium carbonate
    p300.pick_up_tip(tip200['A5'])
    p300.aspirate(125, reservoir['A2'])
    p300.dispense(125, sample_plate['A1'])
    p300.aspirate(125, reservoir['A2'])
    p300.dispense(125, sample_plate['A1'])
    count = 0

    while count < 60:
        p300.mix(1, 50, sample_plate['A1'].bottom(z=0.5))
        protocol.delay(minutes=0.0167)
        count = count + 1

    protocol.delay(minutes=1)
    mag.engage(height_from_base=7.5)
    protocol.delay(minutes=5)
    mag.disengage()

    protocol.delay(minutes=2)
    p300.aspirate(125, sample_plate['A1'].bottom(z=0.5))
    p300.dispense(125, reservoir['A7'])
    p300.aspirate(120, sample_plate['A1'].bottom(z=0.5))
    p300.dispense(120, reservoir['A7'])

    p300.drop_tip()

    #urea
    p300.pick_up_tip(tip200['A6'])
    p300.aspirate(125, reservoir['A3'])
    p300.dispense(125, sample_plate['A1'])
    p300.aspirate(125, reservoir['A3'])
    p300.dispense(125, sample_plate['A1'])
    count = 0

    while count < 60:
        p300.mix(1, 50, sample_plate['A1'].bottom(z=0.5))
        protocol.delay(minutes=0.0167)
        count = count + 1

    protocol.delay(minutes=1)
    mag.engage(height_from_base=7.5)
    protocol.delay(minutes=5)
    mag.disengage()

    protocol.delay(minutes=2)
    p300.aspirate(125, sample_plate['A1'].bottom(z=0.5))
    p300.dispense(125, reservoir['A8'])
    p300.aspirate(120, sample_plate['A1'].bottom(z=0.5))
    p300.dispense(120, reservoir['A8'])

    p300.drop_tip()

    #step 31+32+33
    #KCL/EPPS 1
    p300.pick_up_tip(tip200['A7'])
    p300.aspirate(125, reservoir['A4'])
    p300.dispense(125, sample_plate['A1'])
    count = 0

    while count < 60:
        p300.mix(1, 25, sample_plate['A1'].bottom(z=0.5))
        protocol.delay(minutes=0.0167)
        count = count + 1

    p300.aspirate(125, sample_plate['A1'].bottom(z=0.5))
    p300.dispense(125, finalsample_plate['A1'].bottom(z=0.5))

    protocol.delay(minutes=1)
    mag.engage(height_from_base=7.5)
    protocol.delay(minutes=5)
    mag.disengage()

    protocol.delay(minutes=2)
    p300.aspirate(120, finalsample_plate['A1'].bottom(z=0.5))
    p300.dispense(120, reservoir['A9'])

    p300.drop_tip()

    #KCL/EPPS 2
    p300.pick_up_tip(tip200['A8'])
    p300.aspirate(125, reservoir['A4'])
    p300.dispense(125, finalsample_plate['A1'])
    count = 0

    while count < 60:
        p300.mix(1, 25, finalsample_plate['A1'].bottom(z=0.5))
        protocol.delay(minutes=0.0167)
        count = count + 1

    protocol.delay(minutes=1)
    mag.engage(height_from_base=7.5)
    protocol.delay(minutes=5)
    mag.disengage()

    protocol.delay(minutes=2)
    p300.aspirate(120, sample_plate['A1'].bottom(z=0.5))
    p300.dispense(120, reservoir['A9'])

    p300.drop_tip()

    #EPPS 1
    p300.pick_up_tip(tip200['A9'])
    p300.aspirate(125, reservoir['A5'])
    p300.dispense(125, finalsample_plate['A1'])
    count = 0

    while count < 60:
        p300.mix(1, 25, finalsample_plate['A1'].bottom(z=0.5))
        protocol.delay(minutes=0.0167)
        count = count + 1

    protocol.delay(minutes=1)
    mag.engage(height_from_base=7.5)
    protocol.delay(minutes=5)
    mag.disengage()

    protocol.delay(minutes=2)
    p300.aspirate(120, finalsample_plate['A1'].bottom(z=0.5))
    p300.dispense(120, reservoir['A10'])

    p300.drop_tip()

    #EPPS 2
    p300.pick_up_tip(tip200['A10'])
    p300.aspirate(125, reservoir['A5'])
    p300.dispense(125, finalsample_plate['A1'])
    count = 0

    while count < 60:
        p300.mix(1, 25, finalsample_plate['A1'].bottom(z=0.5))
        protocol.delay(minutes=0.0167)
        count = count + 1

    protocol.delay(minutes=1)
    mag.engage(height_from_base=7.5)
    protocol.delay(minutes=5)
    mag.disengage()

    protocol.delay(minutes=2)
    p300.aspirate(120, finalsample_plate['A1'].bottom(z=0.5))
    p300.dispense(120, reservoir['A10'])

    p300.drop_tip()

    #EPPS 3
    p300.pick_up_tip(tip200['A11'])
    p300.aspirate(125, reservoir['A5'])
    p300.dispense(125, finalsample_plate['A1'])
    count = 0

    while count < 60:
        p300.mix(1, 25, finalsample_plate['A1'].bottom(z=0.5))
        protocol.delay(minutes=0.0167)
        count = count + 1

    protocol.delay(minutes=1)
    mag.engage(height_from_base=7.5)
    protocol.delay(minutes=5)
    mag.disengage()

    protocol.delay(minutes=2)
    p300.aspirate(120, finalsample_plate['A1'].bottom(z=0.5))
    p300.dispense(120, reservoir['A10'])

    p300.drop_tip()




    #step 33.2
    #hand pippete off all remaining liquid, collect beads