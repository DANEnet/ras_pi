#‘Equinox’ by Absolute Magnitude (George Tuli)

#After hearing about the Sonic Pi 2.0 competition we (three band members) decided this was an opportunity to put our coding skills to the test, and accelerate the journey to fame of our band, Absolute Magnitude. Based on Pachelbel’s Cannon, the song has its roots in classical music, but the electronic style of the song maintains modern music trends, similar to those of ‘Lemon Jelly’.

# 'Equinox' by Absolute Magnitude (George Tuli, Owen Gilbert, Joseph Robbins).
# For the Sonic Pi 2.0 Competition.
 
# Set the volume to 1.
set_volume! 1
 
# Generate 4 bars (32 seconds) of white noise, which gradually becomes louder, sustains, then quickly gets quieter.
define :intro_noise do
  use_synth :pnoise
  play 60, attack: 8, sustain: 23.9, release: 0.1, amp: 0.25
end
 
# Play the drum sample 'loop_amen' for 1 second (at 0.875 of its original rate / speed).
define :drums do
  sample :loop_amen, rate: 0.875, amp: 0.6
  sleep 1
end
 
# Play the pattern of notes which makes the bass line, Pachelbel's Canon (in D).
define :bass do
  use_synth :fm
  play_pattern_timed [:D3, :A2, :B2, :Fs2, :G2, :D3, :G2, :A2], 1, amp: 0.5
end
 
# Play the pattern of notes which makes the intro melody.
define :intro_melody do
  use_synth :tb303
  play_pattern_timed [:D4, :B5, :D5, :D6, :Fs6, :D4, :B5, :D6], 0.25, amp: 0.75
end
 
# Play the pattern of notes which makes the main melody.
define :melody do
    use_synth :saw
    play_pattern_timed [66,67,69, 62,64,66, 59,61,62, 57,61,62, 59,61,62, 57,61,62, 59,61,62, 64,62,64],
                      [0.25,0.25,0.25, 0.5,0.25,0.5, 0.25,0.25,0.25, 0.5,0.25,0.5, 0.25,0.25,0.25, 0.5,0.25,0.5, 0.25,0.25,0.25, 0.5,0.5,0.25], release: 0.6, amp: 0.6
end
 
# Play the last eight notes of the melody, which fade out.  Each note has 10% less volume than the note before it.
define :outro_melody_fade do
  use_synth :tb303
  play :D4
  set_volume! 0.8
  sleep 0.25
  play :B5
  set_volume! 0.7
  sleep 0.25
  play :D5
  set_volume! 0.6
  sleep 0.25
  play :D6
  set_volume! 0.5
  sleep 0.25
  play :Fs6
  set_volume! 0.4
  sleep 0.25
  play :D4
  set_volume! 0.3
  sleep 0.25
  play :B5
  set_volume! 0.2
  sleep 0.25
  play :D6
  set_volume! 0.1
  sleep 0.25
  play :D6, sustain: 0.5, release: 0.5  # The last note will fade out over 0.5 seconds.
end
 
# Play the pattern of notes which makes the melody of the first bridge, and first 1.5 bars of the second birdge.
define :bridge_melody1 do
  use_synth :pulse
  play_pattern_timed [:D4, :B5, :D5, :D6, :Fs6, :D4, :B5, :D6], 0.25, amp: 0.75, release: 0.6, pulse_width: 0.4
end
 
# Play the pattern of notes which makes the melody for the second-last 1/4 bar of the second bridge (before the 'guit_e_slide' sample is played).
define :bridge_melody2 do
  use_synth :pulse
  play_pattern_timed [:D4, :B5, :D5, :D6], 0.25, amp: 0.75, release: 0.6, pulse_width: 0.4
end
 
# Call some of the previously defined functions to make the 'intro' section of the song.
define :intro do
  in_thread(name: :i0){intro_noise}
  in_thread(name: :i1){4.times{bass}}
  in_thread(name: :i2){16.times{intro_melody}}
  sleep 16  # Start the drums half way (16/32) through the intro.
  in_thread(name: :i3){16.times{drums}}
end
 
# Call some of the previously defined functions to make the 'main' section of the song.
define :main1 do
  in_thread(name: :m0){2.times{bass}}
  in_thread(name: :m1){2.times{melody}}
  in_thread(name: :m2){16.times{drums}}
end
 
# Call some of the previously defined functions to make the 'main2' section of the song (for after the bridge).
define :main2 do
  in_thread(name: :m3){4.times{bass}}
  in_thread(name: :m4){4.times{melody}}
  in_thread(name: :m5){32.times{drums}}
end
 
# Call some of the previously defined functions to make the 'first bridge' section of the song.
define :bridge1 do
  in_thread(name: :b0){1.times{bass}}
  in_thread(name: :b1){4.times{bridge_melody1}}
  in_thread(name: :b2){8.times{drums}}
end
 
# Call some of the previously defined functions to make the 'second bridge' section of the song.
define :bridge2 do
  in_thread(name: :b3){2.times{bass}}
  in_thread(name: :b4){6.times{drums}}
  in_thread(name: :b5){3.times{bridge_melody1}}
  sleep 6
  in_thread(name: :b6){bridge_melody2}
  sleep 1
  in_thread(name: :b7){sample :guit_e_slide}
end
 
# Call some of the previously defined functions to make the 'outro' section of the song.
define :outro do
  in_thread(name: :o0){2.times{bass}}
  in_thread(name: :o1){7.times{drums}}
  in_thread(name: :o2){7.times{intro_melody}}
  sleep 14
  in_thread(name: :o3){outro_melody_fade}
end
 
# Call the functions: intro, main, bridge1, bridge2, and outro, to play the song.
intro_noise
sleep 8
intro
sleep 16
main1
sleep 16
bridge1
sleep 8
bridge2
sleep 1
main2
sleep 32
outro
 
# Finally, set the volume to 0, for good measure.
set_volume! 0
