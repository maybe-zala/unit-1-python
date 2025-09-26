# Control Flow - Benchmark: White Noise Machine

Your job for this benchmark is to create a program that simulates a white noise machine. In case you are unfamiliar with white noise machines, here is a description from [sleepfoundation.org](https://www.sleepfoundation.org/best-white-noise-machines).

> White noise machines are popular among many sleepers for their ability to block out unwanted noise and potentially promote more restful sleep. There are a wide number of models on the market, ranging from the very basic to those capable of playing a range of white noise as well as soothing natural sounds.

The white noise machine that you will simulate in this benchmark has the following features:
- It can be turned on and off
- The volume can be increased and decreased
- The kind of noise can be cycled between bright white noise, deep white noise, and ocean waves noise.

To use these features, the user can press the following buttons: `P`, `V+`, `V-`, `S`.
- The `P` button toggles the power. While the white noise machine is turned off, only the power button should be processed. In other words, you can't change the volume or noise while the machine is powered off.
- The `V+` and `V-` buttons increase and decrease the volume. The minimum volume is 0 and the maximum volume is 100. Pressing `V+` or `V-` changes the volume by 10 in the appropriate direction.
- The `S` button cycles to the next sound in the order: bright white, deep white, and ocean surf. After ocean surf, the next sound would be to start over with bright white.

After each user interaction, you should update the state of the white noise machine and display its state. If the user provides the input `quit`, the program should finish.

Here is an example execution. Your program should be formatted identically to the example.

```
Power: Off
> P
Power: On
Volume: 0
Noise: Bright White
> S
Power: On
Volume: 0
Noise: Deep White
> P
Power: Off
> P
Power: On
Volume: 0
Noise: Deep White
> quit
```

### Rubric

The white noise machine:
- [ ] can be powered on and off
    - [ ] ignores `V+`, `V-`, and `S` while powered off
- [ ] can have the volume increase and decrease
    - [ ] minimum: 0
    - [ ] maximum: 100
    - [ ] changes in increments of 10
- [ ] can cycle through noises and repeats
    - [ ] bright -> deep -> ocean surf

### Style Guide

- [ ] Variables should have meaningful names that accurately describe what they refer to.
- [ ] No sloppy/unnecessary/commented out code.