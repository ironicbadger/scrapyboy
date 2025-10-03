---
video_id: "19z3hoOU0h0"
title: "Tailscale Up: Adding out of band resilience to an ISP network"
description: "This talk was given by Moritz Frenzel at Tailscale Up in San Francisco on Wednesday, May 31, 2023...."
channel_name: "Tailscale"
channel_id: "UCcdv38QxPjSMqbt5ffLhJLA"
published_at: "2023-07-07"
duration_seconds: 1144
youtube_url: "https://www.youtube.com/watch?v=19z3hoOU0h0"
thumbnail_url: "https://i.ytimg.com/vi_webp/19z3hoOU0h0/maxresdefault.webp"

# Transcription metadata
transcribed_at: "2025-10-03T16:23:18.444786"
transcription_method: "cpu"
model_used: "base"
language: "en"
word_count: 3175
transcription_time_seconds: 30.8
---

# Tailscale Up: Adding out of band resilience to an ISP network

**[00:00](https://youtube.com/watch?v=19z3hoOU0h0&t=0s)** Also, Dean Auguste, for those who don't know, is probably the German version of Nanok, which might be a bit more used to. And I'm going to present to you today about how we added resilience to our out of band network, even though I will happily take credit for everything set here. Most of the work has been done by my colleague, Michael. I just basically came up with the concept and he then had to do all the dirty work, even though it wasn't so dirty. But let's maybe get started with what an ISP network is. So usually you would say, okay, I'm a user, I connect to the internet, that's it.

**[00:30](https://youtube.com/watch?v=19z3hoOU0h0&t=30s)** But in reality, this more or less comes down to you connecting to a CPE, your wireless access point or whatever is available by your provider. And then that CPE over various access technologies somehow connects to a PE router, a provider edge router, where you are physically terminated, at least in the sense of fiber for TSL, that's a whole other story.

**[00:54](https://youtube.com/watch?v=19z3hoOU0h0&t=54s)** And one of those PE routers mostly isn't enough, so they usually are able to terminate 100 or so users. And so we stack more of them within a point of presence of POP. And these POPs then are interconnected via a so-called IGP interior gateway protocol.

**[01:15](https://youtube.com/watch?v=19z3hoOU0h0&t=75s)** This could be ISIS, this could be other protocols such as OSPF, which you've maybe heard of, or even more fancy modern technologies, but it's just for the sake of speaking the same language here in this talk.

**[01:28](https://youtube.com/watch?v=19z3hoOU0h0&t=88s)** And so this IGP basically distinguishes itself from the EGP, which is the exterior gateway protocol, that it itself is a single failure domain.

**[01:41](https://youtube.com/watch?v=19z3hoOU0h0&t=101s)** So if you somehow manage to do something stupid within that IGP, your whole network goes down, and we somehow have to be resilient against that.

**[01:51](https://youtube.com/watch?v=19z3hoOU0h0&t=111s)** So with that out of the way, let me quickly give a quick recap what it is we are doing.

**[01:58](https://youtube.com/watch?v=19z3hoOU0h0&t=118s)** So global ways itself is a national provider in Stuttgart, that's in the bottom left corner of Germany. And there we operate roughly 360 km of dark fiber network, but we operate all over Germany and have over 1000 CPEs in the field.

**[02:14](https://youtube.com/watch?v=19z3hoOU0h0&t=134s)** Within Stuttgart itself, we have 15 of those so-called POPs, two additional bonds, and Frankfurt, one in Berlin, one in Munich. And we use basically Cisco and Juniper orders to connect everything together and use OSPF as our IGP, as well as some other protocols.

**[02:30](https://youtube.com/watch?v=19z3hoOU0h0&t=150s)** And for this talk, we want to focus on basically adding resilience to our core network here. So mainly those 19 POPs, the ASR-9Ks, the Juniper QFXs, and DMX-2-4s.

**[02:42](https://youtube.com/watch?v=19z3hoOU0h0&t=162s)** So how would you usually build such an OOB network? You would have some sort of OOB stack, sort of devices that connect the serial consoles of the orders, and then buy a third party uplink from another ISP that hopefully, at least most of the times, won't break during the same time that you go down.

**[03:02](https://youtube.com/watch?v=19z3hoOU0h0&t=182s)** So at least due to the solutions there. But when you're operating a municipal network, as we are, the main advantage of building that network is that no one else is there because then you have customers. And so we can't do that.

**[03:18](https://youtube.com/watch?v=19z3hoOU0h0&t=198s)** We have to somehow find a possibility to connect at least to another POP in the smallings or in the hope that catastrophic failure only happens within a POP, but never within the whole network. And so what we did is basically use our optical multiplexes.

**[03:34](https://youtube.com/watch?v=19z3hoOU0h0&t=214s)** These are these things called DWDM here, as well as optical amplifiers, the nice triangle behind me, to take a signal from the POP-A and transport it over our dark fiber network towards POP-B and vice versa.

**[03:49](https://youtube.com/watch?v=19z3hoOU0h0&t=229s)** So in so far for theory and practice, this looked like, like you can see here, on the very top you have a very small blue box running Linux. It's a PC engines APU-2.

**[04:01](https://youtube.com/watch?v=19z3hoOU0h0&t=241s)** We've been running Debian on there. And then at the very bottom, you can see a very old Cisco 25.09. For those of you who are aware of ancient technologies has a 10 megabit half duplex interface running AUI.

**[04:16](https://youtube.com/watch?v=19z3hoOU0h0&t=256s)** So this definitely was due for an upgrade. And in between we had a Juniper switch that was running as a media converter to convert from fiber to copper because both the Cisco and the APU were running on copper.

**[04:30](https://youtube.com/watch?v=19z3hoOU0h0&t=270s)** So where feasible obviously we ordered a a out of band circuit from another provider or if not, then we connected to the other POPs.

**[04:40](https://youtube.com/watch?v=19z3hoOU0h0&t=280s)** And to tie everything together, we had open VPN running on a virtual and redundant concentrator, also running on Debian. And we wouldn't be here if that also wouldn't be due for an upgrade.

**[04:53](https://youtube.com/watch?v=19z3hoOU0h0&t=293s)** Our main issues with that is obviously first and foremost in Stuttgart we didn't find third party carriers in most of our locations. We had three devices to manage and maintain and those three devices conservatively draw about a hundred watts of power, which is quite a lot given that they should only be there in case of catastrophic failure.

**[05:13](https://youtube.com/watch?v=19z3hoOU0h0&t=313s)** And this very quickly adds up as we'll see in the end.

**[05:17](https://youtube.com/watch?v=19z3hoOU0h0&t=317s)** The main issue, though, we had is that building redundant open VPN is an interesting story and having failed work, especially when you needed to, at least never happened to us, even though we've tried our very best on about 20 years of experience and running open VPN.

**[05:34](https://youtube.com/watch?v=19z3hoOU0h0&t=334s)** Again, also when we link over to the other POPs, we require a working EDFA, so the optical amplifier there, if this one breaks, then the network or the other band network goes down as well.

**[05:44](https://youtube.com/watch?v=19z3hoOU0h0&t=344s)** And if somehow we manage to not only break just one POP, but the entire network, the entire IGP, then we're shit out of luck.

**[05:54](https://youtube.com/watch?v=19z3hoOU0h0&t=354s)** So to fix that, we set ourselves some design goals. We wanted to reduce our footprint there. We wanted to reduce the operational toil. We wanted to reduce the power draw and we wanted, especially to get rid of that VPN concentrator.

**[06:08](https://youtube.com/watch?v=19z3hoOU0h0&t=368s)** We wanted to be resilient against IGP failures. And therefore, we wanted to use some sort of 3G, 4G, 5G, whatever technology to at least get some IP connectivity in that POP.

**[06:19](https://youtube.com/watch?v=19z3hoOU0h0&t=379s)** It doesn't have to be fast, serial consoles often operate at 9,600, so really speed is not an issue here. And as an added bonus, we wanted to add perimeter security.

**[06:29](https://youtube.com/watch?v=19z3hoOU0h0&t=389s)** So three problems to solve, one being the hardware, second being the cellular connectivity and 30 VPN, the solution to number three will surprise you.

**[06:40](https://youtube.com/watch?v=19z3hoOU0h0&t=400s)** So after scouring the markets and seeing what's available, we landed with open gear. Those are very nice small devices. They have a SFP and a copper port.

**[06:52](https://youtube.com/watch?v=19z3hoOU0h0&t=412s)** They have dual SIM slots that allow even for failover of multiple carriers and multiple SIMs. They have for Ethernet ports, which allow also our users to just connect their laptop when they are in the POP, but also to add other parameters such as UPS or something that is in the POP.

**[07:09](https://youtube.com/watch?v=19z3hoOU0h0&t=429s)** And then they had for serial ports, and you can even extend that with four more serial ports using USB to FTDI cables, so in total, you can manage eight devices with those small small things.

**[07:21](https://youtube.com/watch?v=19z3hoOU0h0&t=441s)** They also have two digital IO ports, which we will use for perimeter security. And the best thing is they run Linux and they actually take care of giving you full CLI access and offering you persistent file system storage.

**[07:33](https://youtube.com/watch?v=19z3hoOU0h0&t=453s)** So everything we do on there is even persistent across system updates. So that was the hardware issue solved.

**[07:41](https://youtube.com/watch?v=19z3hoOU0h0&t=461s)** Next up, we had to worry about cellular connectivity. Most of our POPs are in underground train stations. And so luckily, they also have some base stations of 4G and 5G operators in Stuttgart, but sadly our sites are determined that we just couldn't go with T-Mobile or in Deutsche Telekom as it's called in Germany.

**[08:01](https://youtube.com/watch?v=19z3hoOU0h0&t=481s)** So we had to find a solution to have more than one mobile carrier there. And so we found wherever some they even operate in the US, which basically offer you 2G up to 5G SIM cards and just allows you to have one SIM for all service operators.

**[08:18](https://youtube.com/watch?v=19z3hoOU0h0&t=498s)** And the SIM just has intelligence built in, I guess I have no idea about how mobile networks work, but it automatically selects the best carrier that is available there.

**[08:27](https://youtube.com/watch?v=19z3hoOU0h0&t=507s)** And also tweak the settings. And basically it also should just pop in a SIM card select the APN and have cellular connectivity in all POPs, which is really great.

**[08:37](https://youtube.com/watch?v=19z3hoOU0h0&t=517s)** Also for us, this this network should never be used because it would mean we have a catastrophic failure. However, if it does break, we still want to have some data there.

**[08:48](https://youtube.com/watch?v=19z3hoOU0h0&t=528s)** So it's really a balancing act on how many commitment you give on your data plan there. And so wherever SIM offers data pulling across all our SIMs all over Germany, which quite which reduces the cost as well.

**[09:01](https://youtube.com/watch?v=19z3hoOU0h0&t=541s)** It would also offer IP second private APN, but for VPN, we wanted to go a bit different route, especially for the entire company.

**[09:10](https://youtube.com/watch?v=19z3hoOU0h0&t=550s)** So as mentioned, we have 20 years of experience with VPNs, especially open VPN, but we were never happy with it and we were so we were in the market, especially since it was too much work to maintain.

**[09:23](https://youtube.com/watch?v=19z3hoOU0h0&t=563s)** Why I got full mesh at the time, obviously sounded like a a perfect opportunity for us with the point to point connections. We we lose the concentrator with kernel five six. We get great speed out of it, not relevant here, but for for the overall organization and it has a quite reduced complexity compared to open VPN, especially when looking at ciphers.

**[09:43](https://youtube.com/watch?v=19z3hoOU0h0&t=583s)** But as you know, key management is still a thing commercial support, even especially at the time when we did this was not that greatly available.

**[09:51](https://youtube.com/watch?v=19z3hoOU0h0&t=591s)** We still needed a firewall, whatever IP tables and if tables sort of like for our ACLs and the full mesh configuration requires clever automation.

**[10:02](https://youtube.com/watch?v=19z3hoOU0h0&t=602s)** So we found this tool called tail scale, I'm not sure if you heard of it. And yeah, basically we ticked all our boxes, it builds the full mesh that handles the key rotation, the ACLs are much less pain to maintain for us, because after all we are an ISP, we're not here to spend our money or resources on running a VPN.

**[10:24](https://youtube.com/watch?v=19z3hoOU0h0&t=624s)** We're here to serve our customers. And this was our, yeah, basically our main selling point, obviously yes, it costs money. But ever since we've joined tail scale roughly two years ago, I've never had to worry about VPN ever since in the whole organization, not only with that out of band network.

**[10:39](https://youtube.com/watch?v=19z3hoOU0h0&t=639s)** So we run it everywhere and we're really happy with it.

**[10:42](https://youtube.com/watch?v=19z3hoOU0h0&t=642s)** Obviously, yes, relying on some cloud software is is a factor for us, but I have never had an issue. So good, good job, everyone at tail scale.

**[10:51](https://youtube.com/watch?v=19z3hoOU0h0&t=651s)** The main issue we have is with RFC six, five, nine, eight. And for those of you who don't know, it's the one hundred dot sixty four slash ten address space that tail scale uses internally, it's actually meant for CG net.

**[11:03](https://youtube.com/watch?v=19z3hoOU0h0&t=663s)** CG net is done by ISP so we have some address conflicts here, but we had some good conversations yesterday over dinner, I'm sure we'll find a way to work around this.

**[11:14](https://youtube.com/watch?v=19z3hoOU0h0&t=674s)** I personally would prefer going V6 only, but there are some challenges to solve. Also bonus point for us, obviously was the open source software.

**[11:23](https://youtube.com/watch?v=19z3hoOU0h0&t=683s)** So taking this and putting it all together, basically meant buying the open gear, installing tail scale on it, pop in a verrorism and be happy.

**[11:34](https://youtube.com/watch?v=19z3hoOU0h0&t=694s)** We then have a configuration option on the open gear, which allows you to set up a watchdog that basically just pings around the my p over each interface.

**[11:43](https://youtube.com/watch?v=19z3hoOU0h0&t=703s)** So whenever an interface goes down the default route of the open gear devices magically removed and we were wondering how to solve that with tail scale, but it just automatically fixed itself, which was really nice.

**[11:58](https://youtube.com/watch?v=19z3hoOU0h0&t=718s)** So good job as well.

**[12:00](https://youtube.com/watch?v=19z3hoOU0h0&t=720s)** So if we look at it, installing tail scale was really easy, we just use the prebuilt packages have a bit of bash magic that installs them.

**[12:08](https://youtube.com/watch?v=19z3hoOU0h0&t=728s)** We don't get kernel support because those open gear devices run a three dot something kernel, but as mentioned, nine thousand six hundred about that that even works without kernel support.

**[12:20](https://youtube.com/watch?v=19z3hoOU0h0&t=740s)** And then we just wrote a bit of Python code added some zero touch provisioning it. Now we can easily provision new of those devices. You can see one that is currently serving our pop in Berlin right there.

**[12:33](https://youtube.com/watch?v=19z3hoOU0h0&t=753s)** Then we wanted to have monitoring here. So we sadly had to go the SNMP route. I personally am too young for SNMP and I'm of the oppression that it should slowly leave us, but it is what it is.

**[12:49](https://youtube.com/watch?v=19z3hoOU0h0&t=769s)** And then also we had to file a buck with open gear because it was not RFC 3021 compliant that is using a slash 31st transfer network, which for us is peace is always a quite usable thing because wasting public IP addresses giving the market price of 50 bucks in IP is actually quite painful.

**[13:09](https://youtube.com/watch?v=19z3hoOU0h0&t=789s)** So open gear kindly enough fixed that for us a while ago, so you're free to use it in the future. And then basically what we left with is this very nice graph on a dashboard you can see here, especially interesting is at the very top those green bars that show us how our doors are behaving.

**[13:29](https://youtube.com/watch?v=19z3hoOU0h0&t=809s)** If you ever had remote hands in a data center and then seeing the invoice thereafter, you have a very good way now to challenge them if the actual remote hands task was two hours or four hours, which they really don't like, but tough luck.

**[13:46](https://youtube.com/watch?v=19z3hoOU0h0&t=826s)** Aside from this, we were able to basically monitor everything we can see how stable or unstable LTE is which bands are used and what to do next with it.

**[13:56](https://youtube.com/watch?v=19z3hoOU0h0&t=836s)** And so this mainly concluded our project, we had some lessons learned here, first and foremost, tail scale is just simply amazing, also the open gears just work and wherever some just works for us, it was one of those few IT projects that actually just go as planned and are in time and in budget.

**[14:18](https://youtube.com/watch?v=19z3hoOU0h0&t=858s)** Then the best lesson learned was that a fully matched VPN is really amazing, especially in catastrophic IGP Australia scenarios, please don't ask me how I know, but maybe where we'll tell the story.

**[14:32](https://youtube.com/watch?v=19z3hoOU0h0&t=872s)** So we had a we had a we see in our routing configuration and the whole network went dark and this was at the time where we were still evaluating this and just had the first open gear with tail scale installed.

**[14:46](https://youtube.com/watch?v=19z3hoOU0h0&t=886s)** And yeah, we had an issue, so I actually asked one of our colleagues to just grab that better open gear, run into this data center and plug it into one of our core orders so we can actually do a work and it just worked, which really saved our butts and reduced the downtown there because otherwise we would have to have someone sitting in the data center for a few hours and configure everything.

**[15:09](https://youtube.com/watch?v=19z3hoOU0h0&t=909s)** As mentioned, the door contacts themselves are also very amazing for verifying those remote hands builds.

**[15:16](https://youtube.com/watch?v=19z3hoOU0h0&t=916s)** And then another painful lesson to learn was that if you have remote hands to install your out of band network and kind of kink the serial cable a bit and produce a short on it and you plug it into the routing engine of one of your core orders, they don't like that.

**[15:34](https://youtube.com/watch?v=19z3hoOU0h0&t=934s)** And so crashed and caused another outage, but yeah, I guess nothing to blame anyone except the remote hands for and obviously those guys who thought that just because there is a packet loop on a serial level, the router should crash, but hey, we survived.

**[15:51](https://youtube.com/watch?v=19z3hoOU0h0&t=951s)** And another lesson learned and I'm going to be completely honest here, we didn't plan for it, but if we now in retrospect look at the power consumption we have here, reducing our power consumption by roughly 88.5 watts.

**[16:05](https://youtube.com/watch?v=19z3hoOU0h0&t=965s)** Times 19 pops really does add up the saves 6.2 tons of CO2 per year and those 420 grams are still a very conservative measure or metric tons to say, sorry, I'm a bit metric here, but I hope everyone's fine.

**[16:21](https://youtube.com/watch?v=19z3hoOU0h0&t=981s)** But not only it saves the environment, but it also saves quite a lot of money in this case, roughly 7,500 euros a year, which results in a hardware break even less than three years.

**[16:34](https://youtube.com/watch?v=19z3hoOU0h0&t=994s)** So this is also something we are now taking to account when re-evaluating our hardware decisions.

**[16:41](https://youtube.com/watch?v=19z3hoOU0h0&t=1001s)** So what are the next steps? We have to complete a rollout, we are currently at I think 10 of almost 20 pops rolled out, so this will happen in a coming weeks.

**[16:51](https://youtube.com/watch?v=19z3hoOU0h0&t=1011s)** And we will open source the documentation on how to install tail scale and open gear on our GitHub, so feel free to check that out.

**[16:59](https://youtube.com/watch?v=19z3hoOU0h0&t=1019s)** It's not there yet, but I'm hoping we can get this done within the next two weeks.

**[17:03](https://youtube.com/watch?v=19z3hoOU0h0&t=1023s)** We also, because whoever here has ever done SNMP export a knows the pain behind it, we will gladly share our config to the upstream SNMP export a generator.yml file.

**[17:15](https://youtube.com/watch?v=19z3hoOU0h0&t=1035s)** So you don't have to do this again if you want to implement it.

**[17:18](https://youtube.com/watch?v=19z3hoOU0h0&t=1038s)** And then we've also added a small console tool and let me maybe hope that the demo gods are ever in my favor.

**[17:27](https://youtube.com/watch?v=19z3hoOU0h0&t=1047s)** So I have some time to spare.

**[17:33](https://youtube.com/watch?v=19z3hoOU0h0&t=1053s)** Yeah, give me a second.

**[17:46](https://youtube.com/watch?v=19z3hoOU0h0&t=1066s)** So bigger you said.

**[17:51](https://youtube.com/watch?v=19z3hoOU0h0&t=1071s)** So what we can now do is basically say here console.py and then just a device whose host name I know in the back end is using a net box to find the device itself.

**[18:05](https://youtube.com/watch?v=19z3hoOU0h0&t=1085s)** Then it finds the open gear it's connected to and comes before my password.

**[18:11](https://youtube.com/watch?v=19z3hoOU0h0&t=1091s)** And with that, I am now connected via tail scale to a router in Berlin, Germany.

**[18:19](https://youtube.com/watch?v=19z3hoOU0h0&t=1099s)** Thank you for clapping that was last minute demo I just came up with.

**[18:27](https://youtube.com/watch?v=19z3hoOU0h0&t=1107s)** So yeah, if anyone is interested in that, we'll happily open source it as well, but it's just a no tool you write in a day to save some work.

**[18:37](https://youtube.com/watch?v=19z3hoOU0h0&t=1117s)** And with that out of the way before I yield the floor, I'd like to invite you to join us for a denog in Berlin.

**[18:44](https://youtube.com/watch?v=19z3hoOU0h0&t=1124s)** If you ever wanted to, it's as mentioned in one of the biggest conferences of network operators in even Europe.

**[18:51](https://youtube.com/watch?v=19z3hoOU0h0&t=1131s)** So feel free to come by if you want to.

**[18:53](https://youtube.com/watch?v=19z3hoOU0h0&t=1133s)** And with that, I'm done. Thank you so much for having me.

---

*Automatically generated transcript. May contain errors.*
