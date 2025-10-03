---
video_id: "O4vN3Cwj0pQ"
title: "What's new in Tailscale 1.86? | The Tailscale Changelog Show"
description: "Join us for the first ever Tailscale Changelog Show where we discuss what's new in Tailscale 1.86 for July 2025.

https://tailscale.com/changelog#2025-07-29

Alex, Poppy, and Jay take you through the ..."
channel_name: "Tailscale"
channel_id: "UCcdv38QxPjSMqbt5ffLhJLA"
published_at: "2025-07-31"
duration_seconds: 1549
youtube_url: "https://www.youtube.com/watch?v=O4vN3Cwj0pQ"
thumbnail_url: "https://i.ytimg.com/vi/O4vN3Cwj0pQ/maxresdefault.jpg"

# Transcription metadata
transcribed_at: "2025-10-03T17:52:53.355446"
transcription_method: "cpu"
model_used: "base"
language: "en"
word_count: 4419
transcription_time_seconds: 42.1
---

# What's new in Tailscale 1.86? | The Tailscale Changelog Show

**[00:00](https://youtube.com/watch?v=O4vN3Cwj0pQ&t=0s)** Welcome into a brand new format here on the Tailscale YouTube channel. My name's Alex, and I'm joined by a couple of Tailscales fantastic solutions engineers. My name's Jay Stapleton. I've been with Tailscale for about three and a half years. So in the startup world, that seems like a really long time, and I work on our new business team. And I'm Poppy. I'm one of our solution engineers, but you can probably tell. I'm based in the UK over here, and I work across

**[00:30](https://youtube.com/watch?v=O4vN3Cwj0pQ&t=30s)** our commercial verticals, so working with existing customers on how to best utilize Tailscale. Fantastic. So we have three different countries represented on the Callsdale, America, Canada and the UK, all of which Tailscale has many customers in, and fantastic. Okay. So let's jump on with the show. What we're going to do today is discuss the Tailscale change log. We were all having a little chat the other day, and we were looking through the release notes for 1.86, which is the version of Tailscale that accompanies this, this here video. And looking at some of the features

**[01:00](https://youtube.com/watch?v=O4vN3Cwj0pQ&t=60s)** going, it'd be kind of cool if we just jumped on Mike and did a little just little chat about these things. So Jay, you're at the top of the dock talking about TS State encrypted. What's that business all about? Yeah, one of the things that some of our larger commercial customers have asked us about is encrypting the Tailscale State file at rest. And the Tailscale State file consists of all of the encryption keys that are used to both identify

**[01:30](https://youtube.com/watch?v=O4vN3Cwj0pQ&t=90s)** as well as encrypt the data for machines to communicate with. And it is stored on a file on disk on many platforms. It's a little different between the operating systems. But this new feature allows us to use a TPM to store an encryption key we can use to encrypt this state file when it is on disk.

**[01:59](https://youtube.com/watch?v=O4vN3Cwj0pQ&t=119s)** So am I right in thinking that that is kind of in the same realm as that browser session hijacking like the cookie session hijacking stuff you can do, where if you copy enough of my cookie folder, you can pretend to be using my Google account, for example.

**[02:17](https://youtube.com/watch?v=O4vN3Cwj0pQ&t=137s)** It's a really similar concept where if somebody theoretically had root on your device and could extract these keys and then shut down the original device, they could use those keys to impersonate your machine on the tailnet.

**[02:34](https://youtube.com/watch?v=O4vN3Cwj0pQ&t=154s)** So this extra layer of security makes that and exceedingly difficult.

**[02:40](https://youtube.com/watch?v=O4vN3Cwj0pQ&t=160s)** So what is that state used for? Is it what you just said where it's like the state is my set of keys to open the front door of the town or like what's the state for?

**[02:53](https://youtube.com/watch?v=O4vN3Cwj0pQ&t=173s)** When you log into tail scale, we take the information from your SSO provider and then we generate a set of keys and the primary use for this key is to identify your machine.

**[03:06](https://youtube.com/watch?v=O4vN3Cwj0pQ&t=186s)** Each machine has a unique key and that is tied to your IP address, which is why tail scale IP addresses are stable, but it is also used to initiate those secure connections with with the other machines on your tailnet.

**[03:24](https://youtube.com/watch?v=O4vN3Cwj0pQ&t=204s)** I guess I wanted to talk about something that very much couples into state encryption, but firstly, for those who aren't necessarily familiar with TPMs, a TPM is a trusted platform module.

**[03:34](https://youtube.com/watch?v=O4vN3Cwj0pQ&t=214s)** And it's basically designed to securely generate and store those cryptographic keys. So as Jay was mentioning, you do have your node key and that is currently stored in your local state file. So still very secure, but you can now just take it that level above and have it signed to the TMP file.

**[03:53](https://youtube.com/watch?v=O4vN3Cwj0pQ&t=233s)** So you've got that additional layer of security. And and then when we talk about encryption, obviously encryption is great, but how are we then actually going to make sure every device is using it, like if we're talking about an organizational perspective, right.

**[04:09](https://youtube.com/watch?v=O4vN3Cwj0pQ&t=249s)** And that's where we've also brought in the state encryption into device posture. And if you haven't used device posture, posture checks basically let you enforce security requirements based on the device itself, so not just the user, so not just the SSO authentication.

**[04:25](https://youtube.com/watch?v=O4vN3Cwj0pQ&t=265s)** So things like what operating version are they using do they have disk encryption enabled do they have an antivirus running on their machine. You can specify all of these posture checks in order for them to access certain resources or access anything in the tailnet.

**[04:41](https://youtube.com/watch?v=O4vN3Cwj0pQ&t=281s)** Now what we've done is brought in yes state encrypted. So that's a new posture check that ties very much in with that state encryption and what that allows you to do is tell whether the tell scale clients state on the device holds that nodes private key. So it's encrypted at rest.

**[04:57](https://youtube.com/watch?v=O4vN3Cwj0pQ&t=297s)** So that means that you can now enforce that devices must be using TPM before they can access specific resources in your tailnet.

**[05:05](https://youtube.com/watch?v=O4vN3Cwj0pQ&t=305s)** So again, it's just that just another layer of security, but all designed to just help you keep things locked down, help you really specify access and take control of not only the users in your tailnet, but also the devices that they're using.

**[05:20](https://youtube.com/watch?v=O4vN3Cwj0pQ&t=320s)** Yeah, this is one of those features that we heard these requests come through in sales calls all the time. So we, I mean, you guys speak to customers all day every day. I think that's part of your day job.

**[05:32](https://youtube.com/watch?v=O4vN3Cwj0pQ&t=332s)** And we hear these requests coming through for certain features. So if you're looking to become a tailscale customer, you can head over to tailscale.com slash BTW to find out more about bringing tail scale to work, but also you can just reach out to one of our fine solutions team right here.

**[05:48](https://youtube.com/watch?v=O4vN3Cwj0pQ&t=348s)** And tell them the things that you need to scale to do to bring it to work. You know, we will, you know, no promises, but we'll add features all the time to support our customers. And this is a perfect example of that.

**[05:59](https://youtube.com/watch?v=O4vN3Cwj0pQ&t=359s)** Yeah, and I think very much aligned with that as well as we have a lot of features, which is fantastic. But often it can mean in the scope of networking, the scope of infrastructure.

**[06:10](https://youtube.com/watch?v=O4vN3Cwj0pQ&t=370s)** I want to achieve something, but I don't know exactly what I need to do with tail scale. And that's really why Jay and myself and the rest of the solution engineering team are here.

**[06:20](https://youtube.com/watch?v=O4vN3Cwj0pQ&t=380s)** We're here to help with those more edge cases, the technical feasibility of tail scale. So yeah, anything at all.

**[06:28](https://youtube.com/watch?v=O4vN3Cwj0pQ&t=388s)** You can always ask the question and equally any feature requests you'd love to see. Obviously everything we do is pretty much open source. You can put a feature requests in our GitHub repo.

**[06:38](https://youtube.com/watch?v=O4vN3Cwj0pQ&t=398s)** And that very much does drive the product development for us.

**[06:41](https://youtube.com/watch?v=O4vN3Cwj0pQ&t=401s)** Yeah, and you can, you can annoy one of our engineers Brad and ping him directly. He loves that.

**[06:49](https://youtube.com/watch?v=O4vN3Cwj0pQ&t=409s)** So how does device posture dovetail into mobile device management? I think you mentioned that briefly.

**[06:57](https://youtube.com/watch?v=O4vN3Cwj0pQ&t=417s)** Yes, so mobile device management again, so device posture and MDM. I look at more from a kind of enterprise larger organizational perspective around how are we enforcing device management when it comes to using the tailnet.

**[07:13](https://youtube.com/watch?v=O4vN3Cwj0pQ&t=433s)** And one of the really cool things that we've actually just brought out with MDM as well is the ability to keep tail scale always on.

**[07:20](https://youtube.com/watch?v=O4vN3Cwj0pQ&t=440s)** So there may be many reasons you want to do this from security to compliance purposes. But if you want to always have tail scale on in the background for your company devices.

**[07:31](https://youtube.com/watch?v=O4vN3Cwj0pQ&t=451s)** That's something you can do with our system policies. So you use always on to do that. What that used to do is just stop people disconnecting from the tailnet. Now it prevents any type of exiting from the clients so they can't close down the client can't log out of the client.

**[07:46](https://youtube.com/watch?v=O4vN3Cwj0pQ&t=466s)** Yeah, I would always recommend that people using device posture and MDM to really refine who can access what. So, for example, if you give mobile devices to your employees, you can enforce the only company owned devices can join the tailnet.

**[08:06](https://youtube.com/watch?v=O4vN3Cwj0pQ&t=486s)** If you give out say Android devices, you can enforce the only Android mobile devices are permitted to join the tailnet and you can go as granular as enforcing it must have a certain tail scale version attached to it.

**[08:19](https://youtube.com/watch?v=O4vN3Cwj0pQ&t=499s)** It must actually be a certain version of Android. There's so much you can do when it comes to enforcing granularity around what devices are able to access what.

**[08:30](https://youtube.com/watch?v=O4vN3Cwj0pQ&t=510s)** We also have integrations with some third party tools that give us more depth and more granularity. So what Poppy was talking about are these postures that are built into tail scale.

**[08:41](https://youtube.com/watch?v=O4vN3Cwj0pQ&t=521s)** But if you're running software like CrowdStrike Falcon, like Intune Pro, Jamf Pro, there's a number of them that we can read from. They can feed us back information about the state of the machine as well, the posture of the machine.

**[08:56](https://youtube.com/watch?v=O4vN3Cwj0pQ&t=536s)** So we can set rules with extra predicates. So instead of saying Alex is allowed to SSH into this server, we can say Alex is allowed to SSH into this server only from a company managed device because it's enrolled in our Intune tenant.

**[09:13](https://youtube.com/watch?v=O4vN3Cwj0pQ&t=553s)** Only if he hasn't turned off disk encryption, only if he's got antivirus software running. So if you decide to shut off your antivirus software, then those machines just disappear off the network and you can't see them anymore.

**[09:27](https://youtube.com/watch?v=O4vN3Cwj0pQ&t=567s)** I'm trying to remember the last time I ran any antivirus software whatsoever was a very long time ago.

**[09:33](https://youtube.com/watch?v=O4vN3Cwj0pQ&t=573s)** It's pretty interesting. So you can use these posture attributes get written as part of your grants and policy file. So you can you can get as specific as you like with this stuff and say like, as you said, Alex can SSH to this specific server in production, as long as he has all of these checks and balances enabled on his system.

**[09:56](https://youtube.com/watch?v=O4vN3Cwj0pQ&t=596s)** But then you can go step further and be like, well, you can only do that on a Tuesday if you want to. And then you can combine that with something like I just in time.

**[10:06](https://youtube.com/watch?v=O4vN3Cwj0pQ&t=606s)** What's it called feature? I guess that says well, Alex can only do that if he then also asks for real time permission from his boss during a maintenance window, something like that can be very handy.

**[10:19](https://youtube.com/watch?v=O4vN3Cwj0pQ&t=619s)** And then that'll be granted for 15 minutes or an hour or whatnot. And when it times out, the machine once again disappears.

**[10:27](https://youtube.com/watch?v=O4vN3Cwj0pQ&t=627s)** Yeah. Because the grants and policy file operate on a default deny model. So unless there is a rule there explicitly allowing something.

**[10:37](https://youtube.com/watch?v=O4vN3Cwj0pQ&t=637s)** The default is to deny hence the name, I guess.

**[10:41](https://youtube.com/watch?v=O4vN3Cwj0pQ&t=641s)** And I've heard a rumor that you're going to be doing a deep dive into the grant syntax video soon.

**[10:49](https://youtube.com/watch?v=O4vN3Cwj0pQ&t=649s)** So I want to put that out there because it's important for me that the video gets done and now that we've set it publicly, it has to.

**[10:58](https://youtube.com/watch?v=O4vN3Cwj0pQ&t=658s)** Yeah. Yeah. It's like it was until this very moment, it was shroding as video. It both did and did not exist. And now it exists. So thanks for that, Jay.

**[11:08](https://youtube.com/watch?v=O4vN3Cwj0pQ&t=668s)** I've been moving all of my lab talent stuff from the ACL syntax to the grant syntax partly to become more familiar with it myself, but also so I can use some of these extra features that we're building in because one of the big changes with moving to a grant syntax is that it's extensible.

**[11:27](https://youtube.com/watch?v=O4vN3Cwj0pQ&t=687s)** So we can do things like rope filtering with via grants and we can do app capabilities and all of these extra layers that lead us into exciting new directions.

**[11:39](https://youtube.com/watch?v=O4vN3Cwj0pQ&t=699s)** Yeah. So for those of you that aren't familiar, grants are tail scales. They're basically ACLs 2.0. They are the future for where tail scale is going in terms of defining access and kind of restricting different things being able to talk to different other things.

**[11:57](https://youtube.com/watch?v=O4vN3Cwj0pQ&t=717s)** ACLs will remain around, but they're not going anyway whatsoever. So don't panic. We have committed publicly to maintaining ACLs until the end of time.

**[12:06](https://youtube.com/watch?v=O4vN3Cwj0pQ&t=726s)** But ACLs won't get any new features. So if you ever want any new shiny stuff like what we're talking about here, you know, with the encrypt state or whatever, you're going to need to move to grounds moving forward.

**[12:17](https://youtube.com/watch?v=O4vN3Cwj0pQ&t=737s)** Now, Alex, there's one more feature that was on our list.

**[12:24](https://youtube.com/watch?v=O4vN3Cwj0pQ&t=744s)** You were talking about our new exit node.

**[12:27](https://youtube.com/watch?v=O4vN3Cwj0pQ&t=747s)** I think it's so cool. So we have a feature built into tail scale called exit nodes, which lets you take all of the traffic from your specific client device and exit that traffic through a specific node on your tail net, hence the name exit node.

**[12:43](https://youtube.com/watch?v=O4vN3Cwj0pQ&t=763s)** But we on top of that also have an automatic exit node suggestion feature that looks at a whole bunch of parameters.

**[12:51](https://youtube.com/watch?v=O4vN3Cwj0pQ&t=771s)** Like there's a whole algorithm that our engineering team have developed to look at a bunch of things like latency between my client node and the exit node and then also throughput and performance to that exit node too.

**[13:03](https://youtube.com/watch?v=O4vN3Cwj0pQ&t=783s)** So for example here in Raleigh, my ISP identifies as if I'm in Atlanta for some reason.

**[13:09](https://youtube.com/watch?v=O4vN3Cwj0pQ&t=789s)** So you would think that the exit node it would select would be one in Atlanta, but actually the exit node I have the best performance to is in Virginia.

**[13:16](https://youtube.com/watch?v=O4vN3Cwj0pQ&t=796s)** Go figure. It's kind of weird, but that's just happens to be what it's doing today.

**[13:20](https://youtube.com/watch?v=O4vN3Cwj0pQ&t=800s)** And it looks at a whole bunch of different things in that kind of algorithm as it's making that decision to decide which exit node is going to give me the best performance.

**[13:28](https://youtube.com/watch?v=O4vN3Cwj0pQ&t=808s)** It's not only for tail scale, managed infrastructure, but also for Mulvad managed infrastructure as well because you can use Mulvad exit nodes as part of your tail net as a first class feature.

**[13:38](https://youtube.com/watch?v=O4vN3Cwj0pQ&t=818s)** What I'm particularly excited about here though is that with the auto exit nodes feature, we can specify on the command line now that I want to use an automatic exit node of any or I can, you know,

**[13:51](https://youtube.com/watch?v=O4vN3Cwj0pQ&t=831s)** limited to a specific subset of it, those exit nodes as well.

**[13:54](https://youtube.com/watch?v=O4vN3Cwj0pQ&t=834s)** I think the big win there when it comes to exit nodes and I love exit nodes.

**[13:58](https://youtube.com/watch?v=O4vN3Cwj0pQ&t=838s)** I'm obviously based in the UK. So geofencing and particularly IP allow listing are kind of the main reasons that I like to use exit nodes.

**[14:06](https://youtube.com/watch?v=O4vN3Cwj0pQ&t=846s)** But the big win here around the exit node auto flag is that you're not having to script any fell over logic anymore.

**[14:13](https://youtube.com/watch?v=O4vN3Cwj0pQ&t=853s)** That's just going to happen automatically. Your clients are just going to adapt. So again, it's alleviating just any and even more administrative headaches that you usually get when you look at more I guess more legacy based systems.

**[14:27](https://youtube.com/watch?v=O4vN3Cwj0pQ&t=867s)** But on the geofencing piece and I always love to mention this.

**[14:33](https://youtube.com/watch?v=O4vN3Cwj0pQ&t=873s)** And exit node is fantastic for that example. So let's say I'm obviously based in the UK I'm governed by GDPR.

**[14:39](https://youtube.com/watch?v=O4vN3Cwj0pQ&t=879s)** So there's certain information that should remain in Europe because we have those compliance compliance regulations in place.

**[14:47](https://youtube.com/watch?v=O4vN3Cwj0pQ&t=887s)** So what I can do is always enforce my traffic going through an EU exit node, even when I have to travel sometimes I'll go to, you know, Vegas and do a tell scale conference.

**[14:56](https://youtube.com/watch?v=O4vN3Cwj0pQ&t=896s)** And I still want to make sure that all my traffic is going through a through an exit node in the UK where possible, but otherwise in the EU.

**[15:03](https://youtube.com/watch?v=O4vN3Cwj0pQ&t=903s)** And what you're saying is in your case, what happened to Vegas doesn't stay in Vegas.

**[15:09](https://youtube.com/watch?v=O4vN3Cwj0pQ&t=909s)** It comes out through. Yeah. Exactly. That comes out through my Apple TV at home, which is, yeah, always on exit node for me.

**[15:19](https://youtube.com/watch?v=O4vN3Cwj0pQ&t=919s)** And exit nodes while you're traveling I think are really important because I've noticed in my travels as I'm going to tailscope conferences, which is most of my travels lately.

**[15:30](https://youtube.com/watch?v=O4vN3Cwj0pQ&t=930s)** That airports and hotels have stopped using encrypted Wi-Fi. I guess the barrier to make it easier to use means that anybody who can put a Wi-Fi adapter into a promiscuous mode

**[15:48](https://youtube.com/watch?v=O4vN3Cwj0pQ&t=948s)** has some visibility into what you're doing. And so anywhere that you don't trust the Wi-Fi, you can tunnel back to a machine that you control before egressing to the public internet.

**[16:00](https://youtube.com/watch?v=O4vN3Cwj0pQ&t=960s)** Yeah, that's a great point. So yeah, a lot of airports now, as you say, have wide open and encrypted Wi-Fi networks, which is mildly terrifying.

**[16:10](https://youtube.com/watch?v=O4vN3Cwj0pQ&t=970s)** Because then they do the captive portal afterwards, even though the captive portal doesn't have a password, you just have to agree to their terms of service and watch a little advert probably and all that stuff is happening unencrypted.

**[16:21](https://youtube.com/watch?v=O4vN3Cwj0pQ&t=981s)** So now on the command line, if you want to make use of this exit node auto suggestion thing, you can type tailscale exit node suggests, and it will print out what it thinks is the most suitable exit node for you.

**[16:37](https://youtube.com/watch?v=O4vN3Cwj0pQ&t=997s)** You can also do a tailscale net check as well to see like what kind of dirt nodes your like what the view of the world your client has of the tailscale network to.

**[16:47](https://youtube.com/watch?v=O4vN3Cwj0pQ&t=1007s)** So like, for example, I can see that my latency to New York is 23 milliseconds to Los Angeles is 70 Honolulu, 121 milliseconds. So there you go.

**[16:57](https://youtube.com/watch?v=O4vN3Cwj0pQ&t=1017s)** So yeah, tailscale exit nodes, you can now automatically suggest, well, you can have tailscale automatically suggest which exit node it thinks is best.

**[17:07](https://youtube.com/watch?v=O4vN3Cwj0pQ&t=1027s)** All right, moving along, I think the last thing we're going to talk about today is, well, recent recent feature releases.

**[17:16](https://youtube.com/watch?v=O4vN3Cwj0pQ&t=1036s)** And what came out in the last month or so was tailnet lock is now in GA.

**[17:22](https://youtube.com/watch?v=O4vN3Cwj0pQ&t=1042s)** Yeah, tailnet lock is another one of those features that really got developed through feedback from our larger commercial customers who wanted a way to do local attestation that's, you know, cryptographically based around which machines should be on their tailnet.

**[17:43](https://youtube.com/watch?v=O4vN3Cwj0pQ&t=1063s)** And have it with keys that only they control so that tailscale even has no ability to make these attestations.

**[17:53](https://youtube.com/watch?v=O4vN3Cwj0pQ&t=1073s)** So how can I trust tailscale without trusting tailscale, right?

**[17:58](https://youtube.com/watch?v=O4vN3Cwj0pQ&t=1078s)** Yeah. So when a machine joins a tailnet that has tailnet locked turned on, it can't communicate until a talent admin has counter signed its key from a trusted machine.

**[18:12](https://youtube.com/watch?v=O4vN3Cwj0pQ&t=1092s)** So you may have four or five signing nodes on your tailnet.

**[18:18](https://youtube.com/watch?v=O4vN3Cwj0pQ&t=1098s)** And when somebody tries to join a new machine, you can do an out of band verification that this is a device that should be on your tailnet and then manually counter sign that key.

**[18:28](https://youtube.com/watch?v=O4vN3Cwj0pQ&t=1108s)** And now it is a first class peer in your tailscale network.

**[18:33](https://youtube.com/watch?v=O4vN3Cwj0pQ&t=1113s)** So in the real world, what do we actually see people using tailnet lock for?

**[18:39](https://youtube.com/watch?v=O4vN3Cwj0pQ&t=1119s)** Compliance is a big one. Tailscale works a lot with companies in finance, in healthcare, in government, other, you know, highly regulated environments.

**[18:51](https://youtube.com/watch?v=O4vN3Cwj0pQ&t=1131s)** And when talking to these auditors, they will often come with the worst case scenario and say, if everything goes pear shaped, what is your stock gap to prevent information leakage there?

**[19:05](https://youtube.com/watch?v=O4vN3Cwj0pQ&t=1145s)** And tailnet lock is sort of a big hammer there, saying that no matter what happens anywhere else in the world, I need to counter sign these keys before these machines can communicate.

**[19:19](https://youtube.com/watch?v=O4vN3Cwj0pQ&t=1159s)** And because this is all being done with strong encryption, you know, there's really no way around that.

**[19:27](https://youtube.com/watch?v=O4vN3Cwj0pQ&t=1167s)** Yeah, and I think really similar to Jay, my experience being at tailscale is very much for those compliance regulations as we're working with obviously a lot of business accounts.

**[19:38](https://youtube.com/watch?v=O4vN3Cwj0pQ&t=1178s)** But how I started using tailscale was very much of the home lever and tailnet lock was something that I actually put on my own tailnet.

**[19:45](https://youtube.com/watch?v=O4vN3Cwj0pQ&t=1185s)** And basically I'll give access to, you know, friends and family, for various reasons, I don't want that access to be permanent.

**[19:52](https://youtube.com/watch?v=O4vN3Cwj0pQ&t=1192s)** And I don't keep track of my tailnet as much as I should because I'm not an organization.

**[19:57](https://youtube.com/watch?v=O4vN3Cwj0pQ&t=1197s)** And so tailnet lock really does allow me to stop anyone else from.

**[20:02](https://youtube.com/watch?v=O4vN3Cwj0pQ&t=1202s)** Incorrectly adding a node that shouldn't be within my tailnet, so it's it's a nice kind of set it and forget it approach for me in my own home lab.

**[20:12](https://youtube.com/watch?v=O4vN3Cwj0pQ&t=1212s)** And to make sure that that's just staying locked down because of course I'm not paying as much attention anywhere near the level one organization would admit something to you both is that my personal tailnet had 93 devices on it.

**[20:26](https://youtube.com/watch?v=O4vN3Cwj0pQ&t=1226s)** I looked in yesterday. I removed all of the old ones hadn't connected for at least three months. I've only got 37 now.

**[20:35](https://youtube.com/watch?v=O4vN3Cwj0pQ&t=1235s)** That was a lot of old nonsense just sat there that was authenticated to my tailnet really.

**[20:41](https://youtube.com/watch?v=O4vN3Cwj0pQ&t=1241s)** And tailnet lock wouldn't prevent those notes from reconnecting, but it would prevent me from adding new nodes without being a little more intentional about it, I suppose.

**[20:50](https://youtube.com/watch?v=O4vN3Cwj0pQ&t=1250s)** Exactly, exactly, but yeah, hygiene when it comes to nodes, I find particularly on personal tailnets.

**[20:57](https://youtube.com/watch?v=O4vN3Cwj0pQ&t=1257s)** I don't keep up on it as much as I should, so that's on me.

**[21:01](https://youtube.com/watch?v=O4vN3Cwj0pQ&t=1261s)** But hygiene, if you're looking at more scaling perspective, we actually have some really cool tools that our director of solution engineering has built out.

**[21:10](https://youtube.com/watch?v=O4vN3Cwj0pQ&t=1270s)** We want to like bulk remove in active nodes. We actually have a lot of scripts and things that are pre built into the CLI, if you wanted to want it to share that repo at any point.

**[21:19](https://youtube.com/watch?v=O4vN3Cwj0pQ&t=1279s)** It's is really cool what we did.

**[21:21](https://youtube.com/watch?v=O4vN3Cwj0pQ&t=1281s)** Yeah, you are of course referring to Lee Briggs here, who is he's done a few live streams with me over in the on the ask an expert.

**[21:29](https://youtube.com/watch?v=O4vN3Cwj0pQ&t=1289s)** And Jay, I think it's been on a couple of those two, actually, I'll put a link to Jay's GitHub in the description down below for Jack's storm, J a double X storm.

**[21:39](https://youtube.com/watch?v=O4vN3Cwj0pQ&t=1299s)** He's got a couple of really interesting tools in there that that would be Lee's GitHub, not J's GitHub.

**[21:45](https://youtube.com/watch?v=O4vN3Cwj0pQ&t=1305s)** Yes, no, what I mean, not what I say. Thank you. Yes, that's exactly right.

**[21:51](https://youtube.com/watch?v=O4vN3Cwj0pQ&t=1311s)** Now, one of the final things I want to do before we get out of here is do a feature spotlight. I'm going to this this this week, this episode is going to be Alex's choice of a spotlight feature.

**[22:01](https://youtube.com/watch?v=O4vN3Cwj0pQ&t=1321s)** Yeah, so my favorite tail scale feature, well, there's there's two really and I'm not going to talk about tail scale SSH today, because I think I talk about it way too much on the channel as it is the second one is tail scale serve and follow.

**[22:15](https://youtube.com/watch?v=O4vN3Cwj0pQ&t=1335s)** Now, tail scale serve lets you basically take any file, any web service web, you know, web server and put it on to your talent with practically no configuration.

**[22:28](https://youtube.com/watch?v=O4vN3Cwj0pQ&t=1348s)** Are you telling me I don't need to have any of the TLS certificates, because just such a joy for me to do that.

**[22:35](https://youtube.com/watch?v=O4vN3Cwj0pQ&t=1355s)** You mean you don't enjoy going to your DNS provider and getting a token and then putting it into your Acme client and then also making sure that your DNS records are pointed to the right place and then also configuring the reverse proxy to also you mean to say you don't enjoy doing all of those steps because

**[22:51](https://youtube.com/watch?v=O4vN3Cwj0pQ&t=1371s)** surprisingly, you know, because tail scale serve lets you kind of sidestep all of those things. So on the channel, I am forever doing self host applications deploying them with Docker and like spinning things up and throwing them down and who knows where they are at any given moment in time.

**[23:06](https://youtube.com/watch?v=O4vN3Cwj0pQ&t=1386s)** So for me, just the ability to type tail scale serve and then I select a port number that the web service is running on.

**[23:13](https://youtube.com/watch?v=O4vN3Cwj0pQ&t=1393s)** And then I can access through the fully qualified domain name that every tail net gets for free and I don't have to configure anything else in that scenario and it's also available to every other node on my tail net by default.

**[23:25](https://youtube.com/watch?v=O4vN3Cwj0pQ&t=1405s)** I just love it so much.

**[23:29](https://youtube.com/watch?v=O4vN3Cwj0pQ&t=1409s)** And what about if I wanted to share that with somebody on the public internet?

**[23:35](https://youtube.com/watch?v=O4vN3Cwj0pQ&t=1415s)** Yeah, you probably shouldn't. But if you do, if you do want to do that, you can use tail scale funnel which proxies through tail scale owned infrastructure.

**[23:42](https://youtube.com/watch?v=O4vN3Cwj0pQ&t=1422s)** It's quite heavily QS, like for quality of service reasons, like throttled. So like you're not going to be sharing a jelly fin media server through tail scale funnel, for example, because streaming video is just not going to be.

**[23:55](https://youtube.com/watch?v=O4vN3Cwj0pQ&t=1435s)** It's just not what it's designed for. But if you were a developer, I remember it uni actually, we used to email zip files of source code around to each other because Git was too complicated.

**[24:08](https://youtube.com/watch?v=O4vN3Cwj0pQ&t=1448s)** And we used to do it on Facebook Messenger and sent and like we had versions of databases flight. It was just awful.

**[24:15](https://youtube.com/watch?v=O4vN3Cwj0pQ&t=1455s)** But tail scale funnel would have been amazing. I mean, 15 years ago when I was at university, can we just wind the clock back?

**[24:23](https://youtube.com/watch?v=O4vN3Cwj0pQ&t=1463s)** And from a business perspective, funnel can also be useful. Obviously for developers who want to like share a preview from VS code or something like that.

**[24:33](https://youtube.com/watch?v=O4vN3Cwj0pQ&t=1473s)** But in production, it's often used for things like ingesting web hooks. It's like I want to be able to pull in a web hook, but I don't need that machine to be on the public internet other than that one port.

**[24:45](https://youtube.com/watch?v=O4vN3Cwj0pQ&t=1485s)** Because web hooks are relatively little bit with the QOS is not an issue. And it's just a really convenient way of saying, I want a web hook going directly to this machine down in the bowels of my infrastructure that is otherwise invisible to the general public.

**[25:02](https://youtube.com/watch?v=O4vN3Cwj0pQ&t=1502s)** That's pretty cool. I hadn't even thought of that one.

**[25:07](https://youtube.com/watch?v=O4vN3Cwj0pQ&t=1507s)** Well, I think that will probably do us for today. So we're going to release these change log episodes every what, how often does the tail scale client release six, six to eight weeks, something like that?

**[25:19](https://youtube.com/watch?v=O4vN3Cwj0pQ&t=1519s)** Yeah, around that frequency.

**[25:21](https://youtube.com/watch?v=O4vN3Cwj0pQ&t=1521s)** So we'll probably join you to lovely folks again in another six to eight weeks time to record another episode.

**[25:27](https://youtube.com/watch?v=O4vN3Cwj0pQ&t=1527s)** But until then, I've been Alex.

**[25:29](https://youtube.com/watch?v=O4vN3Cwj0pQ&t=1529s)** I've been chair.

**[25:31](https://youtube.com/watch?v=O4vN3Cwj0pQ&t=1531s)** And I've been poppy.

**[25:32](https://youtube.com/watch?v=O4vN3Cwj0pQ&t=1532s)** Thank you so much for watching and I will see you next time. Bye bye.

---

*Automatically generated transcript. May contain errors.*
