---
video_id: "T15t-V9_faU"
title: "Factorio Remote Multiplayer server sharing made EASY!"
description: "Factorio Space Age is here! If you want to set up a Factorio multiplayer server using docker and Linux then today's video will walk you through the process.

In the video, Alex will also cover sharing..."
channel_name: "Tailscale"
channel_id: "UCcdv38QxPjSMqbt5ffLhJLA"
published_at: "2024-10-25"
duration_seconds: 629
youtube_url: "https://www.youtube.com/watch?v=T15t-V9_faU"
thumbnail_url: "https://i.ytimg.com/vi_webp/T15t-V9_faU/maxresdefault.webp"

# Transcription metadata
transcribed_at: "2025-10-03T15:55:02.250804"
transcription_method: "cpu"
model_used: "base"
language: "en"
word_count: 2051
transcription_time_seconds: 18.3
---

# Factorio Remote Multiplayer server sharing made EASY!

**[00:00](https://youtube.com/watch?v=T15t-V9_faU&t=0s)** To celebrate the release of Factorial Space Age this week, I've come outside to touch graphs. To prove to my mother, I can both play my favourite video game and go outside and breathe in some fresh or terminal air here in North Carolina. In today's video though, I'm going to show you how to deploy a Factorial Headless Multiplayer server using Tailscale to connect to it no matter where you are. So the only internet connection I have today is my phone. I am tethered via my phone to my server back at home.

**[00:30](https://youtube.com/watch?v=T15t-V9_faU&t=30s)** I want to show you how to set up that Factorial Headless server in Docker and connect to it from anywhere. You can then use a Tailscale feature called No Sharing to share that node with any of your friends or family that want to play Factorial Multiplayer with you as well.

**[00:47](https://youtube.com/watch?v=T15t-V9_faU&t=47s)** I honestly don't get the time to play that many video games these days anymore, which makes a game like Factorial all the more special to me. I rank it up there in a pantheon of great sim video games alongside sim city 4, transport tycoon, roller coaster tycoon, that kind of thing.

**[01:03](https://youtube.com/watch?v=T15t-V9_faU&t=63s)** So Space Age came out this week, which adds a whole new DLC to the game. And I thought it would be a good time to walk you guys through configuring a Multiplayer Factorial server.

**[01:14](https://youtube.com/watch?v=T15t-V9_faU&t=74s)** And in order to get started, you're going to need somewhere to run the Factorial Headless server. Over here in the Factorial Multiplayer Wiki, it talks about a dedicated headless server.

**[01:25](https://youtube.com/watch?v=T15t-V9_faU&t=85s)** And typically this will be run on a Linux system. Now, in my case, I have a Linux system running in my basement, and I use it for a lot of these videos. In fact, I'm going to remotely connect back to that system using Tailscale.

**[01:38](https://youtube.com/watch?v=T15t-V9_faU&t=98s)** So you can see here, I'm currently logged into my tailnet on the mat client on my laptop. And under my devices, you can see I've got one here called Deep Thought.

**[01:46](https://youtube.com/watch?v=T15t-V9_faU&t=106s)** Now Deep Thought is reachable via SSH. If I type deep thought, hyphen L root, I'm going to connect over Tailscale SSH via my phone's 5G internet connection. Remember, back to my house. I haven't opened any ports in my firewall.

**[02:01](https://youtube.com/watch?v=T15t-V9_faU&t=121s)** I'm just using tailscales natural reversal technology to connect here from the park back to my house. And we're going to need to get docker installed. That's really easily done these days get docker.com.

**[02:12](https://youtube.com/watch?v=T15t-V9_faU&t=132s)** If we simply copy and paste curl here, just the first part of this command curl URL and then pipe that into SH. That's going to run the script from get docker.com and install docker on this box. Now I already have docker installed on here.

**[02:27](https://youtube.com/watch?v=T15t-V9_faU&t=147s)** So I don't need to go ahead and actually run the script. Now with that out of the way, it's time to copy and paste in the docker compose snippet. Now, lucky for you, here's one I made earlier.

**[02:37](https://youtube.com/watch?v=T15t-V9_faU&t=157s)** So in this directory here, I have the compose.yaml file that we're going to need for today's video. A lot of these environment variables, you can actually just ignore completely to be honest.

**[02:46](https://youtube.com/watch?v=T15t-V9_faU&t=166s)** I've got things in here like generate new save and save name, Badger Badger, just because I'm constantly spinning things up and tearing them down as I'm making these videos.

**[02:54](https://youtube.com/watch?v=T15t-V9_faU&t=174s)** But you're going to want to configure this as required for yourself. Now note in here, it talks about token and factorial username.

**[03:03](https://youtube.com/watch?v=T15t-V9_faU&t=183s)** This is referring, if we look in the documentation, this is referring to the factorial website. So if you want to publish a multiplayer server onto the public factorial multiplayer server directory, that's where you would supply that information.

**[03:17](https://youtube.com/watch?v=T15t-V9_faU&t=197s)** But that's not what we're doing today. What we're going to do is create a multiplayer instance that's going to be available just to you on your network and then anybody that you share that with over tail scale.

**[03:29](https://youtube.com/watch?v=T15t-V9_faU&t=209s)** Now pay attention to a couple of things in this file. First of all, the ports. You must specify that this is a UDP port by default.

**[03:37](https://youtube.com/watch?v=T15t-V9_faU&t=217s)** Docker would turn this into a TCP port. Unless you specify UDP, this will not work. So you must specify the slash UDP here on whatever port you decide to expose this server on.

**[03:49](https://youtube.com/watch?v=T15t-V9_faU&t=229s)** So inside this Docker container, a factorial tools slash factorial, this game server instance is listening on port 34197.

**[03:59](https://youtube.com/watch?v=T15t-V9_faU&t=239s)** We're exposing that externally from the container also on port 34197. Now assuming that everything looks good in your Docker compose file, it's time to actually fire up factorial locally.

**[04:10](https://youtube.com/watch?v=T15t-V9_faU&t=250s)** Don't about you, but any day that I get to fire up factorial for working purposes is a good day in my book.

**[04:17](https://youtube.com/watch?v=T15t-V9_faU&t=257s)** Once factorial is loaded up, we want to go ahead and click on the multiplayer option just here. Click on connect to address. Now where do we get this IP address from?

**[04:25](https://youtube.com/watch?v=T15t-V9_faU&t=265s)** We go to our tail scale client, at least on the Mac anyway, network devices, my devices, and then click on deep thought just here.

**[04:34](https://youtube.com/watch?v=T15t-V9_faU&t=274s)** You can also go to the tail scale admin console and search for the name of the machine that you want to connect to as well.

**[04:42](https://youtube.com/watch?v=T15t-V9_faU&t=282s)** So you can get the fully qualified domain name, the IPv6 IP address or the IPv4 address. This is the one I'm going to go for right here is the IPv4 address and then just copy and paste into the connection box just here.

**[04:54](https://youtube.com/watch?v=T15t-V9_faU&t=294s)** Now we also want to append here the port number that we exposed in the Docker compose file earlier on 34197 and then click connect.

**[05:02](https://youtube.com/watch?v=T15t-V9_faU&t=302s)** And remember, we're connected through my phone over tail scale back to the server running in my house with no ports open.

**[05:10](https://youtube.com/watch?v=T15t-V9_faU&t=310s)** I haven't had to worry about port forwarding or installing any kind of crazy special software.

**[05:15](https://youtube.com/watch?v=T15t-V9_faU&t=315s)** Tail scale just punches the natural household in my firewall for me and I have to worry about it at all.

**[05:21](https://youtube.com/watch?v=T15t-V9_faU&t=321s)** And you can see if I go back to the command here, ironic badger joined the game. There we go.

**[05:27](https://youtube.com/watch?v=T15t-V9_faU&t=327s)** Now, there are a couple of things that I ran into whilst filming that I think I should probably put in the video specifically around version numbers.

**[05:34](https://youtube.com/watch?v=T15t-V9_faU&t=334s)** When we're referring to something in factorial time that's around a brand new big release like this, the developers are churning out multiple updates a day sometimes.

**[05:44](https://youtube.com/watch?v=T15t-V9_faU&t=344s)** So you can see here that I'm running factorial space age 2.0.8. I'm just going to stop the container on the server and show you what's going on inside my compose.yaml file.

**[05:53](https://youtube.com/watch?v=T15t-V9_faU&t=353s)** I've actually pinned the Docker image to the same version number as my clients are all running.

**[05:59](https://youtube.com/watch?v=T15t-V9_faU&t=359s)** Now you can find out what this information is by going to the factorial tools Docker Hub page and looking at the various tags that are available here under the tags section.

**[06:08](https://youtube.com/watch?v=T15t-V9_faU&t=368s)** Overview is actually a bit easier to read you might find. So right here, there's a 2.0.8 tag available.

**[06:14](https://youtube.com/watch?v=T15t-V9_faU&t=374s)** So that's the one I plummed into my Docker compose file just here.

**[06:18](https://youtube.com/watch?v=T15t-V9_faU&t=378s)** So if you run into version mismatches and that kind of thing between clients and servers, you can either configure it on the steam side by going into I think it's properties and then beaters just here and then selecting the version of factorial that you want to run explicitly.

**[06:32](https://youtube.com/watch?v=T15t-V9_faU&t=392s)** Or you can go it on the server side or indeed you can do both. You might find your friends are running vastly different versions depending I don't know if they don't know how closely they keep the versions in sync between different operating systems.

**[06:44](https://youtube.com/watch?v=T15t-V9_faU&t=404s)** But if you run into version mismatches, that's how you solve it.

**[06:48](https://youtube.com/watch?v=T15t-V9_faU&t=408s)** Now I'm going to start the factorial server back up again and I'm actually going to disconnect from my tail net.

**[06:53](https://youtube.com/watch?v=T15t-V9_faU&t=413s)** This is the part where if you're sharing it with your friends, this is the part you want to pay attention to.

**[06:57](https://youtube.com/watch?v=T15t-V9_faU&t=417s)** So I'm going to jump from this tail net at xktz at gmail.com to a tail and scales at gmail.com.

**[07:04](https://youtube.com/watch?v=T15t-V9_faU&t=424s)** And you'll notice that well, first of all, the server's lost connection.

**[07:08](https://youtube.com/watch?v=T15t-V9_faU&t=428s)** If I go back to multiplayer and try and connect to this address, it can't connect to that remote server.

**[07:13](https://youtube.com/watch?v=T15t-V9_faU&t=433s)** Of course not because deep thought is not in the tail and scales at gmail tail net.

**[07:19](https://youtube.com/watch?v=T15t-V9_faU&t=439s)** I can show you that by going to tail scale.com and looking at the devices under my tail net page just here.

**[07:26](https://youtube.com/watch?v=T15t-V9_faU&t=446s)** And you can see that if I search for deep thought, in fact you can see there's only six nodes in this tail net, it's not there.

**[07:32](https://youtube.com/watch?v=T15t-V9_faU&t=452s)** So what you as the owner of the primary tail net, the server owner is going to have to do, is go back to your tail net.

**[07:38](https://youtube.com/watch?v=T15t-V9_faU&t=458s)** Note up here for example, I have Alex ktz at gmail.com.

**[07:42](https://youtube.com/watch?v=T15t-V9_faU&t=462s)** I'm going to bring my mouse over the node that I want to share.

**[07:44](https://youtube.com/watch?v=T15t-V9_faU&t=464s)** In this case, that's deep thought.

**[07:46](https://youtube.com/watch?v=T15t-V9_faU&t=466s)** I'm going to click on share and get a share link.

**[07:49](https://youtube.com/watch?v=T15t-V9_faU&t=469s)** You can share via email if you want to, if you know the recipients email address, but I find the link easier.

**[07:53](https://youtube.com/watch?v=T15t-V9_faU&t=473s)** You can make this a reusable link if you want to, I'm just going to do a one time use link just here.

**[07:58](https://youtube.com/watch?v=T15t-V9_faU&t=478s)** Now I'm going to change from this Chrome session that's logged in as Alex ktz into this Chrome session which is logged in as a tail and scales at gmail.com.

**[08:06](https://youtube.com/watch?v=T15t-V9_faU&t=486s)** So this is me simulating inviting somebody else into my tail net.

**[08:10](https://youtube.com/watch?v=T15t-V9_faU&t=490s)** So Alex ktz wants to share a device with you.

**[08:13](https://youtube.com/watch?v=T15t-V9_faU&t=493s)** You can see I'm logged in as a tail and scales at gmail.com and Alex.

**[08:17](https://youtube.com/watch?v=T15t-V9_faU&t=497s)** Okay, that's me. They're both me in this case.

**[08:20](https://youtube.com/watch?v=T15t-V9_faU&t=500s)** But just imagine that there's two separate people.

**[08:23](https://youtube.com/watch?v=T15t-V9_faU&t=503s)** Alex wants to share a device with you.

**[08:25](https://youtube.com/watch?v=T15t-V9_faU&t=505s)** I'm going to click on accept invite.

**[08:27](https://youtube.com/watch?v=T15t-V9_faU&t=507s)** And what you'll see is that this 100 dot IP address matches the IP address that's in my tail net as well.

**[08:34](https://youtube.com/watch?v=T15t-V9_faU&t=514s)** So 118.109, 118.109.

**[08:38](https://youtube.com/watch?v=T15t-V9_faU&t=518s)** So what I can now do if I go up here to my Mac client, I can look under my network devices and see deep thought dot ktz.ts.net.

**[08:46](https://youtube.com/watch?v=T15t-V9_faU&t=526s)** So I can either connect again using the fully qualified domain name or the IP address.

**[08:51](https://youtube.com/watch?v=T15t-V9_faU&t=531s)** We already have the IP address configured in factorial.

**[08:53](https://youtube.com/watch?v=T15t-V9_faU&t=533s)** So why don't we go ahead and use that.

**[08:55](https://youtube.com/watch?v=T15t-V9_faU&t=535s)** If I go ahead now and click connect, it's going to complain that my active mods don't match the server.

**[09:00](https://youtube.com/watch?v=T15t-V9_faU&t=540s)** Okay, fine.

**[09:02](https://youtube.com/watch?v=T15t-V9_faU&t=542s)** I'm going to join the server after restarting factorial.

**[09:06](https://youtube.com/watch?v=T15t-V9_faU&t=546s)** And that's another thing you might run into with your friends, particularly with factorial.

**[09:10](https://youtube.com/watch?v=T15t-V9_faU&t=550s)** Mods are a huge part of the community.

**[09:12](https://youtube.com/watch?v=T15t-V9_faU&t=552s)** And you can see that now I am connected into factorial on the remote Linux server that I can't actually connect to right now because I'm not on that specific tail net.

**[09:22](https://youtube.com/watch?v=T15t-V9_faU&t=562s)** So this is how you would share factorial with multiple friends and family.

**[09:26](https://youtube.com/watch?v=T15t-V9_faU&t=566s)** And as far as I'm aware, at least there's no limit to a number of people you can do no sharing with.

**[09:31](https://youtube.com/watch?v=T15t-V9_faU&t=571s)** The only stipulation is that they all each have their own individual tail nets for you to share that invite with.

**[09:37](https://youtube.com/watch?v=T15t-V9_faU&t=577s)** We do also offer multiple users in a single tail net.

**[09:41](https://youtube.com/watch?v=T15t-V9_faU&t=581s)** For free, you can have up to three users and on our personal plus plan, you can have up to six different users.

**[09:46](https://youtube.com/watch?v=T15t-V9_faU&t=586s)** That's probably best suited to a family with a bunch of known users, that kind of thing.

**[09:50](https://youtube.com/watch?v=T15t-V9_faU&t=590s)** But if you're sharing this with friends that live on the other side of the planet, or you just want to share this with your friends, right.

**[09:57](https://youtube.com/watch?v=T15t-V9_faU&t=597s)** Then I would strongly recommend that you go ahead with the no sharing option instead.

**[10:01](https://youtube.com/watch?v=T15t-V9_faU&t=601s)** The factory must continue to grow, of course.

**[10:04](https://youtube.com/watch?v=T15t-V9_faU&t=604s)** And that is how you share a factorial multiplayer server running in Docker with anybody in the world securely without opening any ports in your firewall.

**[10:13](https://youtube.com/watch?v=T15t-V9_faU&t=613s)** Thank you so much for watching and until next time, I've been Alex from tail scale.

---

*Automatically generated transcript. May contain errors.*
