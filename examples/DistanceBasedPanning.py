"""
A synthesis example that sends Dust, single sample triggers to a resonant band-pass filter.

Rates of the Dusts and frequencies of the filters are modulated by the mouse X and Y positions.
"""

from mmm_python import * 

# instantiate and load the graph
mmm_audio = MMMAudio(128, num_output_channels=4, graph_name="DistanceBasedPanning", package_name="examples")


mmm_audio.start_audio()

# for Wayland use the fake mouse
MMMAudio.fake_mouse()

mmm_audio.stop_audio()

mmm_audio.plot(48000)