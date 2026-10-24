# Midi-Keyboard
This is my week three project for half-life. The design and parts are different from the tutorial and I also made my own footprint for the capacitive touch pads.


# What is it?

As the name suggests, this is a midi keyboard. It essentially sends data to a computer which then transforms those signals into music. This can be used to create melodies when you don't have instruments on hand. It's also very convenient and easy to carry around since the PCB itself is less than 100x100mm. Another reason you may want to make this is because (I'm assuming) it's also fun to just play around with and see what kind of music you can make!


# How is mine different?

My midi keyboard is different than that of the tutorial because my footprint for the capacitive touch pads is different, as well as the layout. I also don't use any sliders because that exceeded the tier 1 budget (mainly due to shipping costs in my area). I also use 9 capacitive touchpads and 2 computer switches as opposed to 7 touchpads and 3 switches. My firmware is also different.

## How is my firmware different?

My firmware uses the template that was given in the tutorial however it is adjusted to my unique project. It accounts for 9 unique capacitive touch pads, two keyboard switches, and no sliders. This makes it my own unique code, not just copying and pasting the code that was given to us. I want to note that I watched youtube videos to learn how to change my code however I also used the google AI overview a little because there were some specific things that I couldn't find tutorials for made by real people online.


# Images

## Finished KiCad PCB (3d view and normal)

### Normal view

<img width="915" height="663" alt="Screenshot 2026-10-23 at 9 22 44 PM" src="https://github.com/user-attachments/assets/3c485773-8f68-4b20-bc22-5676a79a63de" />


### 3d view

#### Front

<img width="660" height="494" alt="Screenshot 2026-10-23 at 9 10 43 PM" src="https://github.com/user-attachments/assets/bf6003ac-7525-47e8-b50a-6c5920a0e92f" />

#### Back

<img width="527" height="390" alt="Screenshot 2026-10-23 at 9 11 20 PM" src="https://github.com/user-attachments/assets/b1d430b0-367f-418b-bde5-a7f3330546c6" />


# BOM

|Item                    |Qty|Supplier  |Cost/item|Total Cost|link|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
|------------------------|---|----------|---------|----------|-----|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|ESP32-S3-ZERO           |1  |AliExpress|$1.81    |$1.81     |https://www.aliexpress.com/item/1005006642715384.html?                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
|SK6812 MINI_E           |3  |AliExpress|$4.83    |$14.49    |https://www.aliexpress.com/item/1005007863635868.html?                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
|360 Rotary Encoder      |1  |AliExpress|$2.78    |$2.78     |https://www.aliexpress.com/item/1005007644083514.html?                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
|Keycaps                 |1  |Amazon    |$1.99    |$1.99     |https://www.amazon.ca/Dye-Subbed-Engraved-Cherry-MX-Mechanical-Cheryy-mx/dp/B0H1M5VVJJ/ref=sr_1_8?crid=31IBWCTARCE3J&dib=eyJ2IjoiMSJ9.3X9RbTJFJmBqfdfAQ1o6SrylQ5LzeQZUHT9f5bB5Vtrtik_js_f6pRRAZ7E8RfF6Pay9h43SubvgaOmxXVnrkj94xZ9x_g1OU49Hjs_OLbDrZEMkO3NDg3UltTatgSiNmjJHTo0eHEYp_u9OCF83F94n886aKqrdNLoplHu8O2Bo3hfFzxwhnufXSA7WZo4PFJ8hGxgKzcVP2PuN_qvE-KKRzUGv7K8SUN9kF38IKRc_r7YuckHQf4V-ec8AtfrSSxQ5HJh1XTK8jn2ZpBo0dbFnfWfdCwKo8BCB5xH33Q8.yUrJWX8nSMT1G7GCBi0HAb9_bSu6bN1ZfSxA-8C2EXI&dib_tag=se&keywords=cherry+mx+keycaps&qid=1792626652&sprefix=%2Caps%2C171&sr=8-8|
|PCB                     |1  |JLCPCB    |$4.00    |$4.00     |https://jlcpcb.com/                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
|Estimated total shipping|1  |          |         |$4.91     |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
