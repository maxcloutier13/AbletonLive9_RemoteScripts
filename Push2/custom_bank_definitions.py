#Embedded file name: /Users/versonator/Jenkins/live/output/mac_64_static/Release/midi-remote-scripts/Push2/custom_bank_definitions.py
from __future__ import absolute_import
from copy import deepcopy
from ableton.v2.base.collection import IndexedDict
from .bank_definitions import BANK_DEFINITIONS as ORIGINAL_DEFINITIONS
from .bank_definitions import PARAMETERS_KEY, MAIN_KEY
from .parameter_slot_description import use
OPTIONS_KEY = 'Options'
SHOW_WAVEFORM_KEY = 'show_waveform'
BANK_DEFINITIONS = deepcopy(ORIGINAL_DEFINITIONS)
BANK_DEFINITIONS['OriginalSimpler'] = IndexedDict(((MAIN_KEY, {PARAMETERS_KEY: ('Zoom',
                    use('Start').if_parameter('Mode').has_value('One-Shot').else_use('Start').if_parameter('Mode').has_value('Slicing').else_use('Start').if_parameter('Mode').has_value('Classic'),
                    use('End').if_parameter('Mode').has_value('One-Shot').else_use('End').if_parameter('Mode').has_value('Slicing').else_use('End').if_parameter('Mode').has_value('Classic'),
                    use('Fade In').if_parameter('Mode').has_value('One-Shot').else_use('Nudge').if_parameter('Mode').has_value('Slicing').else_use('S Start').if_parameter('Mode').has_value('Classic'),
                    use('Fade Out').if_parameter('Mode').has_value('One-Shot').else_use('Playback').if_parameter('Mode').has_value('Slicing').else_use('S Length').if_parameter('Mode').has_value('Classic'),
                    use('Transpose').if_parameter('Mode').has_value('One-Shot').else_use('Pad Slicing').if_parameter('Mode').has_value('Slicing').else_use('S Loop Length').if_parameter('Mode').has_value('Classic'),
                    use('Volume').if_parameter('Mode').has_value('One-Shot').else_use('Sensitivity').if_parameter('Mode').has_value('Slicing').else_use('S Loop Fade').if_parameter('Mode').has_value('Classic').and_parameter('Warp').has_value('off').else_use(''),
                    'Mode'),
   OPTIONS_KEY: (use('Loop').if_parameter('Mode').has_value('Classic').else_use('Trigger Mode'),
                 'Warp as X Bars',
                 ':2',
                 'x2',
                 'Normalize',
                 'Crop',
                 'Reverse'),
   SHOW_WAVEFORM_KEY: True}),
 ('Global', {PARAMETERS_KEY: ('Glide Mode',
                    'Glide Time',
                    use('').if_parameter('Mode').has_value('One-Shot').else_use('Voices').if_parameter('Mode').has_value('Classic').else_use('Voices').if_parameter('Mode').has_value('Slicing').and_parameter('Playback').has_value('Poly'),
                    'Transpose',
                    'Detune',
                    'Vol < Vel',
                    'Gain',
                    'Volume'),
   OPTIONS_KEY: ('',
                 use('').if_parameter('Mode').has_value('One-Shot').else_use('Retrigger').if_parameter('Mode').has_value('Classic').else_use('Retrigger').if_parameter('Mode').has_value('Slicing').and_parameter('Playback').has_value('Poly'),
                 '',
                 '',
                 '',
                 '',
                 ''),
   SHOW_WAVEFORM_KEY: True}),
 ('Envelopes', {PARAMETERS_KEY: ('Env. Type',
                    use('Fe On').if_parameter('Env. Type').has_value('Filter').else_use('Pe On').if_parameter('Env. Type').has_value('Pitch').else_use('Ve Attack').if_parameter('Mode').has_value('Classic').else_use('Fade In'),
                    use('Fe Attack').if_parameter('Env. Type').has_value('Filter').else_use('Pe Attack').if_parameter('Env. Type').has_value('Pitch').else_use('Ve Decay').if_parameter('Mode').has_value('Classic').else_use('Fade Out'),
                    use('Fe Decay').if_parameter('Env. Type').has_value('Filter').else_use('Pe Decay').if_parameter('Env. Type').has_value('Pitch').else_use('Ve Sustain').if_parameter('Mode').has_value('Classic').else_use('Volume'),
                    use('Fe Sustain').if_parameter('Env. Type').has_value('Filter').else_use('Pe Sustain').if_parameter('Env. Type').has_value('Pitch').else_use('Ve Release').if_parameter('Mode').has_value('Classic'),
                    use('Fe Release').if_parameter('Env. Type').has_value('Filter').else_use('Pe Release').if_parameter('Env. Type').has_value('Pitch'),
                    use('Fe < Env').if_parameter('Env. Type').has_value('Filter').else_use('Pe < Env').if_parameter('Env. Type').has_value('Pitch'),
                    use('Filter Freq').if_parameter('Env. Type').has_value('Filter').else_use('Transpose').if_parameter('Env. Type').has_value('Pitch')),
   OPTIONS_KEY: ('', '', '', '', '', '', ''),
   SHOW_WAVEFORM_KEY: False}),
 ('Warp', {PARAMETERS_KEY: ('Zoom',
                    'Start',
                    'End',
                    'Warp',
                    use('').if_parameter('Warp').has_value('off').else_use('Warp Mode'),
                    use('').if_parameter('Warp').has_value('off').else_use('Preserve').if_parameter('Warp Mode').has_value('Beats').else_use('Grain Size Tones').if_parameter('Warp Mode').has_value('Tones').else_use('Grain Size Texture').if_parameter('Warp Mode').has_value('Texture').else_use('Formants').if_parameter('Warp Mode').has_value('Pro'),
                    use('').if_parameter('Warp').has_value('off').else_use('Loop Mode').if_parameter('Warp Mode').has_value('Beats').else_use('Flux').if_parameter('Warp Mode').has_value('Texture').else_use('Envelope Complex Pro').if_parameter('Warp Mode').has_value('Pro'),
                    use('').if_parameter('Warp').has_value('off').else_use('Envelope').if_parameter('Warp Mode').has_value('Beats')),
   OPTIONS_KEY: ('Warp as X Bars', ':2', 'x2', '', '', '', ''),
   SHOW_WAVEFORM_KEY: True}),
 ('Filter', {PARAMETERS_KEY: ('F On',
                    use('Filter Type').if_parameter('Filter Type').is_available(True).else_use('Filter Type (Legacy)'),
                    use('Filter Freq'),
                    use('Filter Res').if_parameter('Filter Res').is_available(True).else_use('Filter Res (Legacy)'),
                    use('Filter Circuit - LP/HP').if_parameter('Filter Type').has_value('Lowpass').else_use('Filter Circuit - LP/HP').if_parameter('Filter Type').has_value('Highpass').else_use('Filter Circuit - BP/NO/Morph'),
                    use('Filter Morph').if_parameter('Filter Type').has_value('Morph').else_use('').if_parameter('Filter Type').has_value('Lowpass').and_parameter('Filter Circuit - LP/HP').has_value('Clean').else_use('').if_parameter('Filter Type').has_value('Highpass').and_parameter('Filter Circuit - LP/HP').has_value('Clean').else_use('').if_parameter('Filter Type').has_value('Bandpass').and_parameter('Filter Circuit - BP/NO/Morph').has_value('Clean').else_use('').if_parameter('Filter Type').has_value('Notch').and_parameter('Filter Circuit - BP/NO/Morph').has_value('Clean').else_use('Filter Drive'),
                    'Filt < Vel',
                    'Filt < LFO'),
   OPTIONS_KEY: (use('Filter Slope').if_parameter('F On').has_value('on'),
                 '',
                 '',
                 '',
                 '',
                 '',
                 '')}),
 ('LFO', {PARAMETERS_KEY: ('L On',
                    'L Wave',
                    use('L Rate').if_parameter('L Sync').has_value('Free').else_use('L Sync Rate'),
                    'L Attack',
                    'L R < Key',
                    'Vol < LFO',
                    'L Retrig',
                    'L Offset'),
   OPTIONS_KEY: ('',
                 use('LFO Sync Type').if_parameter('L On').has_value('on'),
                 '',
                 '',
                 '',
                 '',
                 '')}),
 ('Pan', {PARAMETERS_KEY: ('Pan', 'Spread', 'Pan < Rnd', 'Pan < LFO', '', '', '', ''),
   OPTIONS_KEY: ('', '', '', '', '', '', '')})))
BANK_DEFINITIONS['Operator'] = IndexedDict((('Oscillators', {PARAMETERS_KEY: ('Oscillator',
                    use('Osc-A On').if_parameter('Oscillator').has_value('A').else_use('Osc-B On').if_parameter('Oscillator').has_value('B').else_use('Osc-C On').if_parameter('Oscillator').has_value('C').else_use('Osc-D On').if_parameter('Oscillator').has_value('D'),
                    use('Osc-A Wave').if_parameter('Oscillator').has_value('A').else_use('Osc-B Wave').if_parameter('Oscillator').has_value('B').else_use('Osc-C Wave').if_parameter('Oscillator').has_value('C').else_use('Osc-D Wave').if_parameter('Oscillator').has_value('D'),
                    use('A Fix On ').if_parameter('Oscillator').has_value('A').else_use('B Fix On ').if_parameter('Oscillator').has_value('B').else_use('C Fix On ').if_parameter('Oscillator').has_value('C').else_use('D Fix On ').if_parameter('Oscillator').has_value('D'),
                    use('A Fix Freq').if_parameter('Oscillator').has_value('A').and_parameter('A Fix On ').has_value('on').else_use('A Coarse').if_parameter('Oscillator').has_value('A').else_use('B Fix Freq').if_parameter('Oscillator').has_value('B').and_parameter('B Fix On ').has_value('on').else_use('B Coarse').if_parameter('Oscillator').has_value('B').else_use('C Fix Freq').if_parameter('Oscillator').has_value('C').and_parameter('C Fix On ').has_value('on').else_use('C Coarse').if_parameter('Oscillator').has_value('C').else_use('D Fix Freq').if_parameter('Oscillator').has_value('D').and_parameter('D Fix On ').has_value('on').else_use('D Coarse').if_parameter('Oscillator').has_value('D'),
                    use('A Fix Freq Mul').if_parameter('Oscillator').has_value('A').and_parameter('A Fix On ').has_value('on').else_use('A Fine').if_parameter('Oscillator').has_value('A').else_use('B Fix Freq Mul').if_parameter('Oscillator').has_value('B').and_parameter('B Fix On ').has_value('on').else_use('B Fine').if_parameter('Oscillator').has_value('B').else_use('C Fix Freq Mul').if_parameter('Oscillator').has_value('C').and_parameter('C Fix On ').has_value('on').else_use('C Fine').if_parameter('Oscillator').has_value('C').else_use('D Fix Freq Mul').if_parameter('Oscillator').has_value('D').and_parameter('D Fix On ').has_value('on').else_use('D Fine').if_parameter('Oscillator').has_value('D'),
                    use('Osc-A Level').if_parameter('Oscillator').has_value('A').else_use('Osc-B Level').if_parameter('Oscillator').has_value('B').else_use('Osc-C Level').if_parameter('Oscillator').has_value('C').else_use('Osc-D Level').if_parameter('Oscillator').has_value('D'),
                    'Algorithm')}),
 ('Osc. Envelopes', {PARAMETERS_KEY: ('Oscillator',
                    use('Osc-A On').if_parameter('Oscillator').has_value('A').else_use('Osc-B On').if_parameter('Oscillator').has_value('B').else_use('Osc-C On').if_parameter('Oscillator').has_value('C').else_use('Osc-D On').if_parameter('Oscillator').has_value('D'),
                    use('Ae Init').if_parameter('Oscillator').has_value('A').else_use('Be Init').if_parameter('Oscillator').has_value('B').else_use('Ce Init').if_parameter('Oscillator').has_value('C').else_use('De Init').if_parameter('Oscillator').has_value('D'),
                    use('Ae Attack').if_parameter('Oscillator').has_value('A').else_use('Be Attack').if_parameter('Oscillator').has_value('B').else_use('Ce Attack').if_parameter('Oscillator').has_value('C').else_use('De Attack').if_parameter('Oscillator').has_value('D'),
                    use('Ae Peak').if_parameter('Oscillator').has_value('A').else_use('Be Peak').if_parameter('Oscillator').has_value('B').else_use('Ce Peak').if_parameter('Oscillator').has_value('C').else_use('De Peak').if_parameter('Oscillator').has_value('D'),
                    use('Ae Decay').if_parameter('Oscillator').has_value('A').else_use('Be Decay').if_parameter('Oscillator').has_value('B').else_use('Ce Decay').if_parameter('Oscillator').has_value('C').else_use('De Decay').if_parameter('Oscillator').has_value('D'),
                    use('Ae Sustain').if_parameter('Oscillator').has_value('A').else_use('Be Sustain').if_parameter('Oscillator').has_value('B').else_use('Ce Sustain').if_parameter('Oscillator').has_value('C').else_use('De Sustain').if_parameter('Oscillator').has_value('D'),
                    use('Ae Release').if_parameter('Oscillator').has_value('A').else_use('Be Release').if_parameter('Oscillator').has_value('B').else_use('Ce Release').if_parameter('Oscillator').has_value('C').else_use('De Release').if_parameter('Oscillator').has_value('D'))}),
 ('Filter', {PARAMETERS_KEY: ('Filter On',
                    use('Filter Type').if_parameter('Filter Type').is_available(True).else_use('Filter Type (Legacy)'),
                    use('Filter Freq'),
                    use('Filter Res').if_parameter('Filter Res').is_available(True).else_use('Filter Res (Legacy)'),
                    use('Filter Circuit - LP/HP').if_parameter('Filter Type').has_value('Lowpass').else_use('Filter Circuit - LP/HP').if_parameter('Filter Type').has_value('Highpass').else_use('Filter Circuit - BP/NO/Morph'),
                    use('Filter Morph').if_parameter('Filter Type').has_value('Morph').else_use('').if_parameter('Filter Type').has_value('Lowpass').and_parameter('Filter Circuit - LP/HP').has_value('Clean').else_use('').if_parameter('Filter Type').has_value('Highpass').and_parameter('Filter Circuit - LP/HP').has_value('Clean').else_use('').if_parameter('Filter Type').has_value('Bandpass').and_parameter('Filter Circuit - BP/NO/Morph').has_value('Clean').else_use('').if_parameter('Filter Type').has_value('Notch').and_parameter('Filter Circuit - BP/NO/Morph').has_value('Clean').else_use('Filter Drive'),
                    'Shaper Type',
                    'Shaper Amt')}),
 ('Filt. Env.', {PARAMETERS_KEY: ('Filter On', 'Fe Init', 'Fe Attack', 'Fe Decay', 'Fe Sustain', 'Fe Release', 'Fe End', 'Fe Amount')}),
 ('Filt. Mod.', {PARAMETERS_KEY: ('Filter On', 'Filt < Vel', 'Filt < LFO', 'Filt < Key', '', '', '', '')}),
 ('LFO', {PARAMETERS_KEY: ('LFO On',
                    'LFO Type',
                    'LFO Range',
                    use('LFO Sync').if_parameter('LFO Range').has_value('Sync').else_use('LFO Rate'),
                    'LFO Amt',
                    'Filt < LFO',
                    use('Oscillator').if_parameter('LFO On').has_value('on'),
                    use('Osc-A < LFO').if_parameter('Oscillator').has_value('A').else_use('Osc-B < LFO').if_parameter('Oscillator').has_value('B').else_use('Osc-C < LFO').if_parameter('Oscillator').has_value('C').else_use('Osc-D < LFO').if_parameter('Oscillator').has_value('D'))}),
 ('LFO Env.', {PARAMETERS_KEY: ('LFO On', 'Le Init', 'Le Attack', 'Le Decay', 'Le Sustain', 'Le Release', 'Le End', 'LFO Amt')}),
 ('Pitch', {PARAMETERS_KEY: ('Transpose',
                    'Spread',
                    'Glide On',
                    'Glide Time',
                    'Pe R < Vel',
                    'LFO < Pe',
                    use('Oscillator').if_parameter('Pe On').has_value('on'),
                    use('Osc-A < Pe').if_parameter('Oscillator').has_value('A').else_use('Osc-B < Pe').if_parameter('Oscillator').has_value('B').else_use('Osc-C < Pe').if_parameter('Oscillator').has_value('C').else_use('Osc-D < Pe').if_parameter('Oscillator').has_value('D'))}),
 ('Pitch Env.', {PARAMETERS_KEY: ('Pe On', 'Pe Init', 'Pe Attack', 'Pe DecayPe Sustain', 'Pe Release', 'Pe End', 'Pe Amount')}),
 ('Global', {PARAMETERS_KEY: ('Panorama', 'Pan < Rnd', 'Pan < Key', 'Filt < Key', 'Time', 'Time < Key', 'Tone', 'Volume')}),
 ('Modulation', {PARAMETERS_KEY: ('Oscillator',
                    use('Osc-A Lev < Vel').if_parameter('Oscillator').has_value('A').else_use('Osc-B Lev < Vel').if_parameter('Oscillator').has_value('B').else_use('Osc-C Lev < Vel').if_parameter('Oscillator').has_value('C').else_use('Osc-D Lev < Vel').if_parameter('Oscillator').has_value('D'),
                    use('A Freq<Vel').if_parameter('Oscillator').has_value('A').else_use('B Freq<Vel').if_parameter('Oscillator').has_value('B').else_use('C Freq<Vel').if_parameter('Oscillator').has_value('C').else_use('D Freq<Vel').if_parameter('Oscillator').has_value('D'),
                    use('A Quantize').if_parameter('Oscillator').has_value('A').else_use('B Quantize').if_parameter('Oscillator').has_value('B').else_use('C Quantize').if_parameter('Oscillator').has_value('C').else_use('D Quantize').if_parameter('Oscillator').has_value('D'),
                    use('Osc-A Retrig').if_parameter('Oscillator').has_value('A').else_use('Osc-B Retrig').if_parameter('Oscillator').has_value('B').else_use('Osc-C Retrig').if_parameter('Oscillator').has_value('C').else_use('Osc-D Retrig').if_parameter('Oscillator').has_value('D'),
                    use('Osc-A Phase').if_parameter('Oscillator').has_value('A').else_use('Osc-B Phase').if_parameter('Oscillator').has_value('B').else_use('Osc-C Phase').if_parameter('Oscillator').has_value('C').else_use('Osc-D Phase').if_parameter('Oscillator').has_value('D'),
                    'LFO Dst B',
                    'LFO Amt B')})))
BANK_DEFINITIONS['Eq8'] = IndexedDict(((MAIN_KEY, {PARAMETERS_KEY: ('Band',
                    use('1 Filter On A').if_parameter('Band').has_value('1').else_use('2 Filter On A').if_parameter('Band').has_value('2').else_use('3 Filter On A').if_parameter('Band').has_value('3').else_use('4 Filter On A').if_parameter('Band').has_value('4').else_use('5 Filter On A').if_parameter('Band').has_value('5').else_use('6 Filter On A').if_parameter('Band').has_value('6').else_use('7 Filter On A').if_parameter('Band').has_value('7').else_use('8 Filter On A').if_parameter('Band').has_value('8'),
                    use('1 Filter Type A').if_parameter('Band').has_value('1').else_use('2 Filter Type A').if_parameter('Band').has_value('2').else_use('3 Filter Type A').if_parameter('Band').has_value('3').else_use('4 Filter Type A').if_parameter('Band').has_value('4').else_use('5 Filter Type A').if_parameter('Band').has_value('5').else_use('6 Filter Type A').if_parameter('Band').has_value('6').else_use('7 Filter Type A').if_parameter('Band').has_value('7').else_use('8 Filter Type A').if_parameter('Band').has_value('8'),
                    use('1 Frequency A').if_parameter('Band').has_value('1').else_use('2 Frequency A').if_parameter('Band').has_value('2').else_use('3 Frequency A').if_parameter('Band').has_value('3').else_use('4 Frequency A').if_parameter('Band').has_value('4').else_use('5 Frequency A').if_parameter('Band').has_value('5').else_use('6 Frequency A').if_parameter('Band').has_value('6').else_use('7 Frequency A').if_parameter('Band').has_value('7').else_use('8 Frequency A').if_parameter('Band').has_value('8'),
                    use('1 Resonance A').if_parameter('Band').has_value('1').else_use('2 Resonance A').if_parameter('Band').has_value('2').else_use('3 Resonance A').if_parameter('Band').has_value('3').else_use('4 Resonance A').if_parameter('Band').has_value('4').else_use('5 Resonance A').if_parameter('Band').has_value('5').else_use('6 Resonance A').if_parameter('Band').has_value('6').else_use('7 Resonance A').if_parameter('Band').has_value('7').else_use('8 Resonance A').if_parameter('Band').has_value('8'),
                    use('1 Gain A').if_parameter('Band').has_value('1').else_use('2 Gain A').if_parameter('Band').has_value('2').else_use('3 Gain A').if_parameter('Band').has_value('3').else_use('4 Gain A').if_parameter('Band').has_value('4').else_use('5 Gain A').if_parameter('Band').has_value('5').else_use('6 Gain A').if_parameter('Band').has_value('6').else_use('7 Gain A').if_parameter('Band').has_value('7').else_use('8 Gain A').if_parameter('Band').has_value('8'),
                    'Scale',
                    'Output Gain')}),
 ('4 Band', {PARAMETERS_KEY: ('1 Frequency A',
                    use('1 Gain A').if_parameter('1 Filter Type A').has_value('Low Shelf').else_use('1 Gain A').if_parameter('1 Filter Type A').has_value('Bell').else_use('1 Gain A').if_parameter('1 Filter Type A').has_value('High Shelf').else_use('1 Resonance A'),
                    '2 Frequency A',
                    use('2 Gain A').if_parameter('2 Filter Type A').has_value('Low Shelf').else_use('2 Gain A').if_parameter('2 Filter Type A').has_value('Bell').else_use('2 Gain A').if_parameter('2 Filter Type A').has_value('High Shelf').else_use('2 Resonance A'),
                    '3 Frequency A',
                    use('3 Gain A').if_parameter('3 Filter Type A').has_value('Low Shelf').else_use('3 Gain A').if_parameter('3 Filter Type A').has_value('Bell').else_use('3 Gain A').if_parameter('3 Filter Type A').has_value('High Shelf').else_use('3 Resonance A'),
                    '4 Frequency A',
                    use('4 Gain A').if_parameter('4 Filter Type A').has_value('Low Shelf').else_use('4 Gain A').if_parameter('4 Filter Type A').has_value('Bell').else_use('4 Gain A').if_parameter('4 Filter Type A').has_value('High Shelf').else_use('4 Resonance A'))}),
 ('8 x Frequency', {PARAMETERS_KEY: ('1 Frequency A', '2 Frequency A', '3 Frequency A', '4 Frequency A', '5 Frequency A', '6 Frequency A', '7 Frequency A', '8 Frequency A')}),
 ('8 x Gain', {PARAMETERS_KEY: ('1 Gain A', '2 Gain A', '3 Gain A', '4 Gain A', '5 Gain A', '6 Gain A', '7 Gain A', '8 Gain A')}),
 ('8 x Resonance', {PARAMETERS_KEY: ('1 Resonance A', '2 Resonance A', '3 Resonance A', '4 Resonance A', '5 Resonance A', '6 Resonance A', '7 Resonance A', '8 Resonance A')})))