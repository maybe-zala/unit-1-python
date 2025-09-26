# Control Flow - Benchmark: Balloon Clown

In this benchmark, you will make a program that allows the user to specify a fancy balloon that they would like! The user can choose between a sword, dog, or triforce balloon. Each of these balloons allow for a different amount of air before popping. After the user has chosen which balloon they want, they can ask you to pump air into the balloon, release air from the balloon, or tie off the balloon and take it with them. If they pump it up too much, the balloon will pop!

**Details:**

- The sword can hold 5 units of air.
- The dog can hold 7 units of air.
- The triforce can hold 11 units of air.
- Pumping air into the balloon adds 3 units of air.
- Releasing air from the balloon lets 2 units of air out of the balloon.

**Examples:** 

```
I can make a sword, dog, or the triforce.
Which balloon do you want? dog
Balloon: dog
Capacity: 7
Current: 0
[pump] air, [release] air, [tie] balloon> pump
Balloon: dog
Capacity: 7
Current: 3
[pump] air, [release] air, [tie] balloon> pump
Balloon: dog
Capacity: 7
Current: 6
[pump] air, [release] air, [tie] balloon> pump
POP!
```

```
I can make a sword, dog, or the triforce.
Which balloon do you want? triforce
Balloon: triforce
Capacity: 11
Current: 0
[pump] air, [release] air, [tie] balloon> pump
Balloon: triforce
Capacity: 11
Current: 3
[pump] air, [release] air, [tie] balloon> release
Balloon: triforce
Capacity: 11
Current: 1
[pump] air, [release] air, [tie] balloon> release
Balloon: triforce
Capacity: 11
Current: 0
[pump] air, [release] air, [tie] balloon> pump
Balloon: triforce
Capacity: 11
Current: 3
[pump] air, [release] air, [tie] balloon> pump
Balloon: triforce
Capacity: 11
Current: 6
[pump] air, [release] air, [tie] balloon> pump
Balloon: triforce
Capacity: 11
Current: 9
[pump] air, [release] air, [tie] balloon> release
Balloon: triforce
Capacity: 11
Current: 7
[pump] air, [release] air, [tie] balloon> pump
Balloon: triforce
Capacity: 11
Current: 10
[pump] air, [release] air, [tie] balloon> tie
Here is your triforce balloon!
```


### Rubric

- [ ] Ask the user which balloon they want.
  - They should only be allowed to choose sword, dog, or triforce.
- [ ] Capacity is correctly determined based on the balloon.
- [ ] The user can pump up the balloon.
  - Pumping past the capacity causes the balloon to pop.
- [ ] The user can release air from the balloon.
  - You cannot release more air than is in the balloon.
- [ ] The user can tie off the balloon and take it with them.
- [ ] Notify the user if they made an invalid input.

### Style Guide

- [ ] Code should be formatted neatly
- [ ] Variables should have meaningful names that accurately describe what they refer to.
- [ ] No sloppy/unnecessary/commented out code.

