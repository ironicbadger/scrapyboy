---
video_id: "tqvvZhGrciQ"
title: "A deep dive into using Tailscale with Docker"
description: "Everything you ever wanted to know about using Tailscale in a Docker container.

- GitHub resources: https://github.com/tailscale-dev/docker-guide-code-examples
- Tailscale.com blog post: https://tail..."
channel_name: "Tailscale"
channel_id: "UCcdv38QxPjSMqbt5ffLhJLA"
published_at: "2024-02-07"
duration_seconds: 1918
youtube_url: "https://www.youtube.com/watch?v=tqvvZhGrciQ"
thumbnail_url: "https://i.ytimg.com/vi_webp/tqvvZhGrciQ/maxresdefault.webp"

# Transcription metadata
transcribed_at: "2025-10-03T17:39:54.444880"
transcription_method: "cpu"
model_used: "base"
language: "en"
word_count: 5893
transcription_time_seconds: 52.3
---

# A deep dive into using Tailscale with Docker

**[00:00](https://youtube.com/watch?v=tqvvZhGrciQ&t=0s)** About 10 years ago, you are pretty unusual if you are running a container in production, whereas these days, you're unusual if you're not. In today's video, we're going to talk about Tailscale and Docker. We're going to cover how to add a container to your Tailnet, why you might want to consider running Tailscale in a container in the first place, as well as how to use Tailscale Servant Funnel to expose those Tailscale applications from your Tailnet directly to the public internet. Today's video will be quite a long one, so I've put chapter markers down there for you to skip

**[00:30](https://youtube.com/watch?v=tqvvZhGrciQ&t=30s)** around and find a bit of the video that you need, so with that, let's get started.

**[00:36](https://youtube.com/watch?v=tqvvZhGrciQ&t=36s)** The first question that probably comes to mind is, why would I even want to put Tailscale in a container in the first place?

**[00:42](https://youtube.com/watch?v=tqvvZhGrciQ&t=42s)** Well, by putting a container directly onto your Tailnet, that's our term for a Tailscale network, by the way, you can not only control access via ACLs, but you can also replace reverse proxies.

**[00:54](https://youtube.com/watch?v=tqvvZhGrciQ&t=54s)** Yes, for those of you that have been waiting to learn reverse proxies for long enough, I've got good news.

**[00:59](https://youtube.com/watch?v=tqvvZhGrciQ&t=59s)** You don't have to learn them ever, you can just completely skip that step.

**[01:03](https://youtube.com/watch?v=tqvvZhGrciQ&t=63s)** And you can also access any other service on your Tailnet from these containers as well.

**[01:09](https://youtube.com/watch?v=tqvvZhGrciQ&t=69s)** So you can have something running in your basement in your house connected to something in the cloud.

**[01:13](https://youtube.com/watch?v=tqvvZhGrciQ&t=73s)** Take, for example, a GPU workload, some AI workload or something like that.

**[01:18](https://youtube.com/watch?v=tqvvZhGrciQ&t=78s)** You've got something running in a WS or GCP, and you don't want to pay their GPU prices, but you've got a GPU sat in your gaming computer like right here, and you want a way to connect the two together.

**[01:29](https://youtube.com/watch?v=tqvvZhGrciQ&t=89s)** Well, using Tailscale, you can do just that.

**[01:33](https://youtube.com/watch?v=tqvvZhGrciQ&t=93s)** Think of the possibilities, and this all happens through Tailscale's encrypted wire guard based tunnels.

**[01:39](https://youtube.com/watch?v=tqvvZhGrciQ&t=99s)** You don't have to mess around with port forwarding or complex firewall rules or dynamic DNS or any of that.

**[01:46](https://youtube.com/watch?v=tqvvZhGrciQ&t=106s)** It all becomes a thing of the past.

**[01:50](https://youtube.com/watch?v=tqvvZhGrciQ&t=110s)** Tailscale provides an official Docker image that you can find over on Docker Hub as well as GitHub container registry.

**[01:57](https://youtube.com/watch?v=tqvvZhGrciQ&t=117s)** This exposes several parameters through what are called environment variables.

**[02:02](https://youtube.com/watch?v=tqvvZhGrciQ&t=122s)** There'll be a full list of those variables exposed by the container down below.

**[02:07](https://youtube.com/watch?v=tqvvZhGrciQ&t=127s)** There are two primary methods for adding a container to your tailnet.

**[02:11](https://youtube.com/watch?v=tqvvZhGrciQ&t=131s)** Well, three, if we include logging into the container manually, running Tailscale up, copying the resulting printout, logging into the browser manually, and redoing that every single time you bring up a container.

**[02:23](https://youtube.com/watch?v=tqvvZhGrciQ&t=143s)** The two methods we're going to cover today are both what are called programmatic methods.

**[02:27](https://youtube.com/watch?v=tqvvZhGrciQ&t=147s)** So these are ones that you can repeatedly do without any manual intervention.

**[02:32](https://youtube.com/watch?v=tqvvZhGrciQ&t=152s)** The first option is called an auth key, and the second is called an OAuth client.

**[02:37](https://youtube.com/watch?v=tqvvZhGrciQ&t=157s)** And as for which one is right for you, well, it kind of depends, I'm afraid.

**[02:42](https://youtube.com/watch?v=tqvvZhGrciQ&t=162s)** It's just one of those classic situations where it really does depend on what you're going to be doing with it.

**[02:47](https://youtube.com/watch?v=tqvvZhGrciQ&t=167s)** So let's dig into some of the differences between the two.

**[02:50](https://youtube.com/watch?v=tqvvZhGrciQ&t=170s)** Both of these methods actually support most of the same things.

**[02:54](https://youtube.com/watch?v=tqvvZhGrciQ&t=174s)** There's just some nuances that you've got to be aware of when choosing between the two.

**[02:58](https://youtube.com/watch?v=tqvvZhGrciQ&t=178s)** So let's first of all take a look at API access.

**[03:03](https://youtube.com/watch?v=tqvvZhGrciQ&t=183s)** An auth key grants full API level access to any client that authenticates using it.

**[03:09](https://youtube.com/watch?v=tqvvZhGrciQ&t=189s)** This is in contrast to an OAuth client, which limits API access via scoping.

**[03:15](https://youtube.com/watch?v=tqvvZhGrciQ&t=195s)** So this, for example, means if I have an OAuth client secret that is scoped to only allow people to modify the DNS,

**[03:22](https://youtube.com/watch?v=tqvvZhGrciQ&t=202s)** or scoped to only allow people to read and write devices on my tailnet,

**[03:26](https://youtube.com/watch?v=tqvvZhGrciQ&t=206s)** or only scoped to read audit logs, that's all they can do or any combination of those different things as well, by the way.

**[03:34](https://youtube.com/watch?v=tqvvZhGrciQ&t=214s)** Whereas with an auth key, because it grants full API access to anybody that has that secret,

**[03:41](https://youtube.com/watch?v=tqvvZhGrciQ&t=221s)** they can do whatever they want.

**[03:43](https://youtube.com/watch?v=tqvvZhGrciQ&t=223s)** And so if auditors are in your regular vernacular, it's likely that this alone will be enough of a feature for you

**[03:49](https://youtube.com/watch?v=tqvvZhGrciQ&t=229s)** that rules out auth keys in favor of OAuth clients.

**[03:53](https://youtube.com/watch?v=tqvvZhGrciQ&t=233s)** The next thing to look at is expiry and lifespan.

**[03:57](https://youtube.com/watch?v=tqvvZhGrciQ&t=237s)** An auth key has a maximum lifespan of 90 days.

**[04:01](https://youtube.com/watch?v=tqvvZhGrciQ&t=241s)** Now a lot of people think that this means that anything that's authenticated using that auth key,

**[04:06](https://youtube.com/watch?v=tqvvZhGrciQ&t=246s)** also automatically expires after 90 days, this isn't the case.

**[04:11](https://youtube.com/watch?v=tqvvZhGrciQ&t=251s)** It's worth bearing in mind that auth keys are separate from the node keys.

**[04:16](https://youtube.com/watch?v=tqvvZhGrciQ&t=256s)** So under the hood, what happens when you authenticate a client to your tailnet,

**[04:20](https://youtube.com/watch?v=tqvvZhGrciQ&t=260s)** is node keys are generated, so this is underneath is the wire guard key exchange magic that makes tail scale work.

**[04:26](https://youtube.com/watch?v=tqvvZhGrciQ&t=266s)** That is a completely separate expiry process from the authentication token that you use to initiate that process.

**[04:34](https://youtube.com/watch?v=tqvvZhGrciQ&t=274s)** And a lot of people use OAuth clients simply because they never expire.

**[04:38](https://youtube.com/watch?v=tqvvZhGrciQ&t=278s)** Now in practice, what this means is you're going to have to come up with some way to regularly rotate those tokens,

**[04:43](https://youtube.com/watch?v=tqvvZhGrciQ&t=283s)** so that any security posture that you have or any risk profiles you have are met,

**[04:48](https://youtube.com/watch?v=tqvvZhGrciQ&t=288s)** or if you just simply want to set it and forget it type solution,

**[04:51](https://youtube.com/watch?v=tqvvZhGrciQ&t=291s)** and an OAuth client might be right for you.

**[04:53](https://youtube.com/watch?v=tqvvZhGrciQ&t=293s)** But there are plenty of situations where you might want to give someone temporary access

**[04:57](https://youtube.com/watch?v=tqvvZhGrciQ&t=297s)** to add something to your tailnet and then have that auth key automatically revoked.

**[05:01](https://youtube.com/watch?v=tqvvZhGrciQ&t=301s)** The next important difference is the tagging.

**[05:04](https://youtube.com/watch?v=tqvvZhGrciQ&t=304s)** So when you add a node to your tailnet, it must be owned by somebody.

**[05:09](https://youtube.com/watch?v=tqvvZhGrciQ&t=309s)** And when you use an auth key, that identity by default, at least with an auth key,

**[05:13](https://youtube.com/watch?v=tqvvZhGrciQ&t=313s)** is assumed to be the person who clicked the generate auth key button in the UI.

**[05:18](https://youtube.com/watch?v=tqvvZhGrciQ&t=318s)** You can add tags to an auth key if you would like,

**[05:21](https://youtube.com/watch?v=tqvvZhGrciQ&t=321s)** but with an OAuth client that secret doesn't actually itself add the node to the tailnet,

**[05:26](https://youtube.com/watch?v=tqvvZhGrciQ&t=326s)** it has to assume the identity of a tag owner instead.

**[05:30](https://youtube.com/watch?v=tqvvZhGrciQ&t=330s)** This is because a node on a tailnet must have an owner, whether that's a user or a tag.

**[05:36](https://youtube.com/watch?v=tqvvZhGrciQ&t=336s)** And when you use an auth key, that node is added to your tailnet as the user who generated the key.

**[05:41](https://youtube.com/watch?v=tqvvZhGrciQ&t=341s)** With an OAuth client though, the node is owned by the tag assigned at secret creation time.

**[05:47](https://youtube.com/watch?v=tqvvZhGrciQ&t=347s)** And this is why in our ACLs you will see tags listed as tag owners.

**[05:52](https://youtube.com/watch?v=tqvvZhGrciQ&t=352s)** The OAuth client is assuming ownership of a specific resource on your tailnet using the tag.

**[05:58](https://youtube.com/watch?v=tqvvZhGrciQ&t=358s)** So the tag ownership is assumed using the tag assigned to the client secret at the time of creation.

**[06:05](https://youtube.com/watch?v=tqvvZhGrciQ&t=365s)** So let's walk through adding a container to our tailnet using an auth key.

**[06:10](https://youtube.com/watch?v=tqvvZhGrciQ&t=370s)** I'm using the Visual Studio code tailscale extension here to access a Ubuntu virtual machine

**[06:17](https://youtube.com/watch?v=tqvvZhGrciQ&t=377s)** with Docker pre-installed with Docker Compose ready to go.

**[06:20](https://youtube.com/watch?v=tqvvZhGrciQ&t=380s)** And I have here a sample Docker Compose file.

**[06:23](https://youtube.com/watch?v=tqvvZhGrciQ&t=383s)** There'll be a link to a GitHub repo down below with all of these resources for you,

**[06:28](https://youtube.com/watch?v=tqvvZhGrciQ&t=388s)** as well as the blog post that accompanies this video with all the materials explaining,

**[06:33](https://youtube.com/watch?v=tqvvZhGrciQ&t=393s)** you know, all the details behind this file.

**[06:37](https://youtube.com/watch?v=tqvvZhGrciQ&t=397s)** So let's walk through the Compose file that we've got here.

**[06:40](https://youtube.com/watch?v=tqvvZhGrciQ&t=400s)** So first of all, online five, we have the tailscale image.

**[06:43](https://youtube.com/watch?v=tqvvZhGrciQ&t=403s)** This is the official tailscale Docker image from Docker Hub.

**[06:47](https://youtube.com/watch?v=tqvvZhGrciQ&t=407s)** Next up, we have the container name.

**[06:49](https://youtube.com/watch?v=tqvvZhGrciQ&t=409s)** So this refers to the name that Docker gives the container on the Ubuntu host.

**[06:54](https://youtube.com/watch?v=tqvvZhGrciQ&t=414s)** Next up, we have the host name.

**[06:56](https://youtube.com/watch?v=tqvvZhGrciQ&t=416s)** Now this is important because this is the name that tailscale will add to this container to the tailnet

**[07:03](https://youtube.com/watch?v=tqvvZhGrciQ&t=423s)** with the name of.

**[07:04](https://youtube.com/watch?v=tqvvZhGrciQ&t=424s)** So whenever we want to use Magic DNS to refer to this container,

**[07:08](https://youtube.com/watch?v=tqvvZhGrciQ&t=428s)** we will use auth key hyphen test.

**[07:10](https://youtube.com/watch?v=tqvvZhGrciQ&t=430s)** You can make this value whatever you like, by the way.

**[07:13](https://youtube.com/watch?v=tqvvZhGrciQ&t=433s)** It doesn't have to match the container name or the service name.

**[07:17](https://youtube.com/watch?v=tqvvZhGrciQ&t=437s)** Next up, we're going to specify our environment variables.

**[07:20](https://youtube.com/watch?v=tqvvZhGrciQ&t=440s)** So here we're specifying our auth key.

**[07:22](https://youtube.com/watch?v=tqvvZhGrciQ&t=442s)** This is basically like a password, remember.

**[07:25](https://youtube.com/watch?v=tqvvZhGrciQ&t=445s)** So just, you know, treat it with care.

**[07:27](https://youtube.com/watch?v=tqvvZhGrciQ&t=447s)** And then the next thing we have here is the state directory.

**[07:30](https://youtube.com/watch?v=tqvvZhGrciQ&t=450s)** The state directory is really important.

**[07:32](https://youtube.com/watch?v=tqvvZhGrciQ&t=452s)** And it's coupled, by the way, with this line here of volume.

**[07:35](https://youtube.com/watch?v=tqvvZhGrciQ&t=455s)** So valib tailscale is the directory that the container is going to use to persist all of the state of, you know,

**[07:43](https://youtube.com/watch?v=tqvvZhGrciQ&t=463s)** what state, when I logged in and authenticated to the tailnet,

**[07:47](https://youtube.com/watch?v=tqvvZhGrciQ&t=467s)** what was my wire guard key exchange underneath, like all of that kind of stuff gets stored in this directory.

**[07:53](https://youtube.com/watch?v=tqvvZhGrciQ&t=473s)** And the reason it's important is because if the container restarts or gets recreated

**[07:57](https://youtube.com/watch?v=tqvvZhGrciQ&t=477s)** or any other kind of major event in the container's lifespan,

**[08:01](https://youtube.com/watch?v=tqvvZhGrciQ&t=481s)** the state gets persisted in this directory.

**[08:04](https://youtube.com/watch?v=tqvvZhGrciQ&t=484s)** And so it doesn't have to reauthenticate to the tailnet every single time.

**[08:08](https://youtube.com/watch?v=tqvvZhGrciQ&t=488s)** We'll get out of sync with what's going on.

**[08:10](https://youtube.com/watch?v=tqvvZhGrciQ&t=490s)** Next up, we have the ton device.

**[08:13](https://youtube.com/watch?v=tqvvZhGrciQ&t=493s)** This is a networking necessity.

**[08:15](https://youtube.com/watch?v=tqvvZhGrciQ&t=495s)** And below it, we have a couple of capabilities that we've added to the container as well.

**[08:20](https://youtube.com/watch?v=tqvvZhGrciQ&t=500s)** So net admin and cis module.

**[08:23](https://youtube.com/watch?v=tqvvZhGrciQ&t=503s)** These three or four lines here mean that we don't need to give this container a privileged status within the kernel.

**[08:30](https://youtube.com/watch?v=tqvvZhGrciQ&t=510s)** So it's a much more secure way of doing it because we're being very explicit with the permissions that we're giving this container with these lines here.

**[08:37](https://youtube.com/watch?v=tqvvZhGrciQ&t=517s)** And then restart unless stopped totally optional.

**[08:40](https://youtube.com/watch?v=tqvvZhGrciQ&t=520s)** You don't need this bit unless you want to.

**[08:42](https://youtube.com/watch?v=tqvvZhGrciQ&t=522s)** Next up, we have the actual web service that we're trying to run here.

**[08:45](https://youtube.com/watch?v=tqvvZhGrciQ&t=525s)** Now this is just a very basic engine ex web container.

**[08:48](https://youtube.com/watch?v=tqvvZhGrciQ&t=528s)** It's not even got a real website in it.

**[08:50](https://youtube.com/watch?v=tqvvZhGrciQ&t=530s)** It's just we're just going to load the engine ex test page on port 80.

**[08:54](https://youtube.com/watch?v=tqvvZhGrciQ&t=534s)** And then finally, we have the network mode.

**[08:56](https://youtube.com/watch?v=tqvvZhGrciQ&t=536s)** Now this is the magic source that connects everything together and makes this whole thing work.

**[09:02](https://youtube.com/watch?v=tqvvZhGrciQ&t=542s)** So network mode service colon TS off key test.

**[09:07](https://youtube.com/watch?v=tqvvZhGrciQ&t=547s)** This is a Docker compose specific incantation.

**[09:10](https://youtube.com/watch?v=tqvvZhGrciQ&t=550s)** So TS off key test here actually refers to the name of the service up online for up here.

**[09:17](https://youtube.com/watch?v=tqvvZhGrciQ&t=557s)** Now if you're doing this with a Docker run command for whatever reason, you can actually replace the name of this with container.

**[09:23](https://youtube.com/watch?v=tqvvZhGrciQ&t=563s)** And then the name of the container.

**[09:25](https://youtube.com/watch?v=tqvvZhGrciQ&t=565s)** So if you know, if this was a TS123, you would you would do TS123 like this.

**[09:31](https://youtube.com/watch?v=tqvvZhGrciQ&t=571s)** And those two things would have to match, but I'm going to use service because I'm in the Docker compose ecosystem.

**[09:36](https://youtube.com/watch?v=tqvvZhGrciQ&t=576s)** So I'm quite happy with doing it like this.

**[09:38](https://youtube.com/watch?v=tqvvZhGrciQ&t=578s)** Now what I'm going to do here.

**[09:40](https://youtube.com/watch?v=tqvvZhGrciQ&t=580s)** Oh, I should probably generate my auth key before I do compose option.

**[09:44](https://youtube.com/watch?v=tqvvZhGrciQ&t=584s)** So let's jump across to our tail scale admin console and go up here to settings.

**[09:49](https://youtube.com/watch?v=tqvvZhGrciQ&t=589s)** And then under settings, we're going to want to jump into the keys section.

**[09:53](https://youtube.com/watch?v=tqvvZhGrciQ&t=593s)** Then we're going to click on generate auth key.

**[09:56](https://youtube.com/watch?v=tqvvZhGrciQ&t=596s)** And then we're just going to give it a name.

**[09:58](https://youtube.com/watch?v=tqvvZhGrciQ&t=598s)** The name can be whatever you like.

**[10:00](https://youtube.com/watch?v=tqvvZhGrciQ&t=600s)** So I'm just going to call this Docker auth key test can be whatever you like.

**[10:04](https://youtube.com/watch?v=tqvvZhGrciQ&t=604s)** It's not important.

**[10:05](https://youtube.com/watch?v=tqvvZhGrciQ&t=605s)** It's going to be a single use key.

**[10:07](https://youtube.com/watch?v=tqvvZhGrciQ&t=607s)** So we're not going to do any reusability or anything like that reusable keys are.

**[10:11](https://youtube.com/watch?v=tqvvZhGrciQ&t=611s)** They're fine, but they're quite risky.

**[10:14](https://youtube.com/watch?v=tqvvZhGrciQ&t=614s)** So if if you don't treat them with care and you have a key that lasts for 90 days,

**[10:19](https://youtube.com/watch?v=tqvvZhGrciQ&t=619s)** you've effectively given anybody that finds that string of characters root access to your tail net.

**[10:25](https://youtube.com/watch?v=tqvvZhGrciQ&t=625s)** You know, they can add and remove devices.

**[10:27](https://youtube.com/watch?v=tqvvZhGrciQ&t=627s)** There is no scoping remember for an auth key.

**[10:30](https://youtube.com/watch?v=tqvvZhGrciQ&t=630s)** So anybody that has this key can do whatever they like to your tail net programmatically.

**[10:35](https://youtube.com/watch?v=tqvvZhGrciQ&t=635s)** So just bear that in mind and treat it with care.

**[10:38](https://youtube.com/watch?v=tqvvZhGrciQ&t=638s)** Next up, we've got the expiration.

**[10:40](https://youtube.com/watch?v=tqvvZhGrciQ&t=640s)** I'm going to set this to 90 days.

**[10:42](https://youtube.com/watch?v=tqvvZhGrciQ&t=642s)** Now, there is a bit of a misconception around expiration.

**[10:45](https://youtube.com/watch?v=tqvvZhGrciQ&t=645s)** A lot of folks seem to think that if the container gets to 90 days and you authenticated using an auth key that expires after 90 days,

**[10:52](https://youtube.com/watch?v=tqvvZhGrciQ&t=652s)** that container is going to drop off your tail net and completely need a new auth key bang on 90 days.

**[10:58](https://youtube.com/watch?v=tqvvZhGrciQ&t=658s)** It's not quite the case.

**[10:59](https://youtube.com/watch?v=tqvvZhGrciQ&t=659s)** The keys we use to authenticate the node to the tail net are different from the wire guard keys that get exchanged behind the scenes later on.

**[11:07](https://youtube.com/watch?v=tqvvZhGrciQ&t=667s)** Those keys are good for about four months or so.

**[11:10](https://youtube.com/watch?v=tqvvZhGrciQ&t=670s)** And you can disable key expiry if you want to in the tail scan admin console as well.

**[11:14](https://youtube.com/watch?v=tqvvZhGrciQ&t=674s)** So theoretically, you could use an auth key with a one day expiry set your key expiry to disabled.

**[11:22](https://youtube.com/watch?v=tqvvZhGrciQ&t=682s)** And that container would stay on a tail net until the end of time.

**[11:25](https://youtube.com/watch?v=tqvvZhGrciQ&t=685s)** Another setting that's worth exploring is ephemeral.

**[11:27](https://youtube.com/watch?v=tqvvZhGrciQ&t=687s)** So if you're doing something with CICD continuous integration,

**[11:31](https://youtube.com/watch?v=tqvvZhGrciQ&t=691s)** maybe you have a GitHub action that wants to talk to something off site.

**[11:35](https://youtube.com/watch?v=tqvvZhGrciQ&t=695s)** For example, it's not part of the GitHub ecosystem.

**[11:38](https://youtube.com/watch?v=tqvvZhGrciQ&t=698s)** Those jobs are typically short lived.

**[11:40](https://youtube.com/watch?v=tqvvZhGrciQ&t=700s)** So you don't necessarily want those containers on your tail net forever.

**[11:45](https://youtube.com/watch?v=tqvvZhGrciQ&t=705s)** So an ephemeral node will automatically remove itself after it goes offline.

**[11:50](https://youtube.com/watch?v=tqvvZhGrciQ&t=710s)** I don't want this in this case, but it can be very useful in certain situations.

**[11:54](https://youtube.com/watch?v=tqvvZhGrciQ&t=714s)** And now we come to tags.

**[11:56](https://youtube.com/watch?v=tqvvZhGrciQ&t=716s)** We talked about tags a little bit earlier,

**[11:58](https://youtube.com/watch?v=tqvvZhGrciQ&t=718s)** but this is where you would set a tag as it pertains to a specific auth key.

**[12:02](https://youtube.com/watch?v=tqvvZhGrciQ&t=722s)** And you can set multiple tags here if you want to.

**[12:05](https://youtube.com/watch?v=tqvvZhGrciQ&t=725s)** I don't really want any tags on this node.

**[12:07](https://youtube.com/watch?v=tqvvZhGrciQ&t=727s)** I want this node to be authenticated as my user.

**[12:09](https://youtube.com/watch?v=tqvvZhGrciQ&t=729s)** So I'm just going to leave this empty.

**[12:11](https://youtube.com/watch?v=tqvvZhGrciQ&t=731s)** I'm going to click on generate key.

**[12:13](https://youtube.com/watch?v=tqvvZhGrciQ&t=733s)** And then I'm going to copy this to my clipboard,

**[12:15](https://youtube.com/watch?v=tqvvZhGrciQ&t=735s)** go back to my Docker compose file,

**[12:17](https://youtube.com/watch?v=tqvvZhGrciQ&t=737s)** and just enter the value that we had on our clipboard.

**[12:21](https://youtube.com/watch?v=tqvvZhGrciQ&t=741s)** Click save.

**[12:22](https://youtube.com/watch?v=tqvvZhGrciQ&t=742s)** Now I can do my Docker compose up.

**[12:25](https://youtube.com/watch?v=tqvvZhGrciQ&t=745s)** I'm going to create a couple of containers.

**[12:28](https://youtube.com/watch?v=tqvvZhGrciQ&t=748s)** You can see there's a whole bunch of stuff scrolling by here.

**[12:32](https://youtube.com/watch?v=tqvvZhGrciQ&t=752s)** The auth key has appeared.

**[12:34](https://youtube.com/watch?v=tqvvZhGrciQ&t=754s)** The containers appeared in my town.

**[12:36](https://youtube.com/watch?v=tqvvZhGrciQ&t=756s)** You can see that in the VS code dashboard just there.

**[12:38](https://youtube.com/watch?v=tqvvZhGrciQ&t=758s)** If I go back to my admin console,

**[12:41](https://youtube.com/watch?v=tqvvZhGrciQ&t=761s)** notice that my single use key has actually automatically invalidated itself.

**[12:46](https://youtube.com/watch?v=tqvvZhGrciQ&t=766s)** Remember, it was a single use key.

**[12:48](https://youtube.com/watch?v=tqvvZhGrciQ&t=768s)** So automatically puts itself in the recently invalidated auth keys section down here.

**[12:54](https://youtube.com/watch?v=tqvvZhGrciQ&t=774s)** And then on my machines page,

**[12:56](https://youtube.com/watch?v=tqvvZhGrciQ&t=776s)** we can see that if I look at auth key test,

**[12:58](https://youtube.com/watch?v=tqvvZhGrciQ&t=778s)** I now have a container that's in here.

**[13:01](https://youtube.com/watch?v=tqvvZhGrciQ&t=781s)** So if I go to HTTP auth key hyphen test,

**[13:05](https://youtube.com/watch?v=tqvvZhGrciQ&t=785s)** which is the DNS name that we set in our host name,

**[13:08](https://youtube.com/watch?v=tqvvZhGrciQ&t=788s)** remember, just here auth key hyphen test.

**[13:10](https://youtube.com/watch?v=tqvvZhGrciQ&t=790s)** We can actually refer to this container by its host name,

**[13:14](https://youtube.com/watch?v=tqvvZhGrciQ&t=794s)** by its magic DNS name,

**[13:15](https://youtube.com/watch?v=tqvvZhGrciQ&t=795s)** and resolve the URL that's running the web page.

**[13:18](https://youtube.com/watch?v=tqvvZhGrciQ&t=798s)** Now, ngx is running on port 80 underneath,

**[13:20](https://youtube.com/watch?v=tqvvZhGrciQ&t=800s)** so it's just a plain HTTP request.

**[13:23](https://youtube.com/watch?v=tqvvZhGrciQ&t=803s)** And we're actually connecting,

**[13:24](https://youtube.com/watch?v=tqvvZhGrciQ&t=804s)** we'll dig into the specifics a little bit later on.

**[13:27](https://youtube.com/watch?v=tqvvZhGrciQ&t=807s)** But we're actually connecting to port 80 of this container,

**[13:29](https://youtube.com/watch?v=tqvvZhGrciQ&t=809s)** which has attached itself to the interface of your tail scale container.

**[13:34](https://youtube.com/watch?v=tqvvZhGrciQ&t=814s)** But that's how we get started with an auth key.

**[13:36](https://youtube.com/watch?v=tqvvZhGrciQ&t=816s)** Let's now look at OAuth clients.

**[13:39](https://youtube.com/watch?v=tqvvZhGrciQ&t=819s)** Let's start by looking at the differences between an OAuth client and an auth key.

**[13:44](https://youtube.com/watch?v=tqvvZhGrciQ&t=824s)** So I've got a second Docker compose YAML file here,

**[13:48](https://youtube.com/watch?v=tqvvZhGrciQ&t=828s)** which you'll notice is pretty similar to the Docker compose on the left.

**[13:52](https://youtube.com/watch?v=tqvvZhGrciQ&t=832s)** So on the left we have the auth key,

**[13:54](https://youtube.com/watch?v=tqvvZhGrciQ&t=834s)** and on the right we have the OAuth client.

**[13:57](https://youtube.com/watch?v=tqvvZhGrciQ&t=837s)** You'll notice that we're actually even using the same environment variable.

**[14:00](https://youtube.com/watch?v=tqvvZhGrciQ&t=840s)** Okay, we've added an extra one with TS extra args.

**[14:04](https://youtube.com/watch?v=tqvvZhGrciQ&t=844s)** This is where we specify the container tag

**[14:07](https://youtube.com/watch?v=tqvvZhGrciQ&t=847s)** that the auth client uses,

**[14:09](https://youtube.com/watch?v=tqvvZhGrciQ&t=849s)** the OAuth client uses when it brings up the container.

**[14:12](https://youtube.com/watch?v=tqvvZhGrciQ&t=852s)** So when the container starts,

**[14:14](https://youtube.com/watch?v=tqvvZhGrciQ&t=854s)** it's running something called container boot.

**[14:16](https://youtube.com/watch?v=tqvvZhGrciQ&t=856s)** This does a tail scale up command under the scenes.

**[14:20](https://youtube.com/watch?v=tqvvZhGrciQ&t=860s)** And it recognizes that we've provided an OAuth client secret.

**[14:24](https://youtube.com/watch?v=tqvvZhGrciQ&t=864s)** It then uses that secret to generate an auth key under the covers

**[14:28](https://youtube.com/watch?v=tqvvZhGrciQ&t=868s)** with the specific tag that we've associated here.

**[14:31](https://youtube.com/watch?v=tqvvZhGrciQ&t=871s)** Because if you remember when you add a node to a tail net,

**[14:34](https://youtube.com/watch?v=tqvvZhGrciQ&t=874s)** it has to be owned by somebody.

**[14:37](https://youtube.com/watch?v=tqvvZhGrciQ&t=877s)** And tags and users are all sort of in this melond of ownership.

**[14:41](https://youtube.com/watch?v=tqvvZhGrciQ&t=881s)** And so when we add the node with the tag container,

**[14:45](https://youtube.com/watch?v=tqvvZhGrciQ&t=885s)** we're authenticating that node as if it belongs to that specific tag owner.

**[14:50](https://youtube.com/watch?v=tqvvZhGrciQ&t=890s)** Generating an OAuth client secrets quite straightforward.

**[14:53](https://youtube.com/watch?v=tqvvZhGrciQ&t=893s)** So again, we're going to jump back to our tail scale admin console.

**[14:57](https://youtube.com/watch?v=tqvvZhGrciQ&t=897s)** Go to settings, go to OAuth clients over here on the left.

**[15:00](https://youtube.com/watch?v=tqvvZhGrciQ&t=900s)** Click generate OAuth client.

**[15:03](https://youtube.com/watch?v=tqvvZhGrciQ&t=903s)** I'm going to select devices right.

**[15:05](https://youtube.com/watch?v=tqvvZhGrciQ&t=905s)** And notice that the read permission is automatically set.

**[15:08](https://youtube.com/watch?v=tqvvZhGrciQ&t=908s)** I'm just going to write test 123 for the description.

**[15:11](https://youtube.com/watch?v=tqvvZhGrciQ&t=911s)** It's totally optional, by the way.

**[15:13](https://youtube.com/watch?v=tqvvZhGrciQ&t=913s)** And under tags here, tag container.

**[15:15](https://youtube.com/watch?v=tqvvZhGrciQ&t=915s)** I'll just show you real quick where I set that up in my ACLs.

**[15:18](https://youtube.com/watch?v=tqvvZhGrciQ&t=918s)** I just have a tag container here,

**[15:20](https://youtube.com/watch?v=tqvvZhGrciQ&t=920s)** which is owned by the group auto group admin.

**[15:23](https://youtube.com/watch?v=tqvvZhGrciQ&t=923s)** Remember, there'll be a link down below to all of the details,

**[15:26](https://youtube.com/watch?v=tqvvZhGrciQ&t=926s)** like the big Git repository with my ACL file,

**[15:29](https://youtube.com/watch?v=tqvvZhGrciQ&t=929s)** just so you can copy and paste if you want to,

**[15:31](https://youtube.com/watch?v=tqvvZhGrciQ&t=931s)** as well as the linked blog post.

**[15:33](https://youtube.com/watch?v=tqvvZhGrciQ&t=933s)** So if we go back to OAuth clients over here,

**[15:36](https://youtube.com/watch?v=tqvvZhGrciQ&t=936s)** we've got the tag container.

**[15:38](https://youtube.com/watch?v=tqvvZhGrciQ&t=938s)** And then we just click generate client.

**[15:40](https://youtube.com/watch?v=tqvvZhGrciQ&t=940s)** The client ID isn't particularly important to us here.

**[15:43](https://youtube.com/watch?v=tqvvZhGrciQ&t=943s)** But the client secret treats it like a password once again,

**[15:46](https://youtube.com/watch?v=tqvvZhGrciQ&t=946s)** same as with an auth key.

**[15:48](https://youtube.com/watch?v=tqvvZhGrciQ&t=948s)** I'm going to go back to VS code and just copy in my value here.

**[15:52](https://youtube.com/watch?v=tqvvZhGrciQ&t=952s)** I'm going to click save.

**[15:54](https://youtube.com/watch?v=tqvvZhGrciQ&t=954s)** And then just going to change into the correct directory.

**[15:57](https://youtube.com/watch?v=tqvvZhGrciQ&t=957s)** And then do a Docker compose up.

**[16:00](https://youtube.com/watch?v=tqvvZhGrciQ&t=960s)** And this is going to add a second container to my tailnet now,

**[16:03](https://youtube.com/watch?v=tqvvZhGrciQ&t=963s)** using the name TS OAuth test.

**[16:06](https://youtube.com/watch?v=tqvvZhGrciQ&t=966s)** Actually, not quite.

**[16:08](https://youtube.com/watch?v=tqvvZhGrciQ&t=968s)** In line seven, it'll just be OAuth test.

**[16:10](https://youtube.com/watch?v=tqvvZhGrciQ&t=970s)** So if we go over here to my machines page,

**[16:14](https://youtube.com/watch?v=tqvvZhGrciQ&t=974s)** we can see that OAuth test is there.

**[16:16](https://youtube.com/watch?v=tqvvZhGrciQ&t=976s)** Also note that expiry is disabled.

**[16:19](https://youtube.com/watch?v=tqvvZhGrciQ&t=979s)** Nodes that are added to your tailnet using an OAuth client

**[16:23](https://youtube.com/watch?v=tqvvZhGrciQ&t=983s)** do not expire.

**[16:25](https://youtube.com/watch?v=tqvvZhGrciQ&t=985s)** So that's a big difference between an auth key

**[16:28](https://youtube.com/watch?v=tqvvZhGrciQ&t=988s)** and an OAuth client authenticated node.

**[16:31](https://youtube.com/watch?v=tqvvZhGrciQ&t=991s)** And by default, nodes are also added as ephemeral.

**[16:35](https://youtube.com/watch?v=tqvvZhGrciQ&t=995s)** So in order to make a node non-ephemeral,

**[16:38](https://youtube.com/watch?v=tqvvZhGrciQ&t=998s)** we'll have to stop the container,

**[16:40](https://youtube.com/watch?v=tqvvZhGrciQ&t=1000s)** remove the state directory that we have.

**[16:42](https://youtube.com/watch?v=tqvvZhGrciQ&t=1002s)** So TS OAuth test.

**[16:44](https://youtube.com/watch?v=tqvvZhGrciQ&t=1004s)** By the way, that is this directory here.

**[16:46](https://youtube.com/watch?v=tqvvZhGrciQ&t=1006s)** They remember where the state gets stored

**[16:48](https://youtube.com/watch?v=tqvvZhGrciQ&t=1008s)** when the node authenticates to the tailnet.

**[16:50](https://youtube.com/watch?v=tqvvZhGrciQ&t=1010s)** We'll remove that directory as pseudo.

**[16:55](https://youtube.com/watch?v=tqvvZhGrciQ&t=1015s)** And then we need to just add onto the end of our auth key

**[16:58](https://youtube.com/watch?v=tqvvZhGrciQ&t=1018s)** just here ephemeral equals false.

**[17:02](https://youtube.com/watch?v=tqvvZhGrciQ&t=1022s)** We also need to make sure it's deleted

**[17:04](https://youtube.com/watch?v=tqvvZhGrciQ&t=1024s)** from your tailnet as well in your admin console.

**[17:07](https://youtube.com/watch?v=tqvvZhGrciQ&t=1027s)** Then bring the save the compose file.

**[17:10](https://youtube.com/watch?v=tqvvZhGrciQ&t=1030s)** And then bring the node back up again with Docker compose up.

**[17:13](https://youtube.com/watch?v=tqvvZhGrciQ&t=1033s)** And if we go back to our admin console,

**[17:15](https://youtube.com/watch?v=tqvvZhGrciQ&t=1035s)** we will see that the OAuth node appears,

**[17:17](https://youtube.com/watch?v=tqvvZhGrciQ&t=1037s)** expires is still disabled,

**[17:19](https://youtube.com/watch?v=tqvvZhGrciQ&t=1039s)** but the node is no longer ephemeral.

**[17:21](https://youtube.com/watch?v=tqvvZhGrciQ&t=1041s)** So it's a really minor difference,

**[17:23](https://youtube.com/watch?v=tqvvZhGrciQ&t=1043s)** but just being able to add that ephemeral equals false

**[17:26](https://youtube.com/watch?v=tqvvZhGrciQ&t=1046s)** on the end means the nodes have a lot more

**[17:28](https://youtube.com/watch?v=tqvvZhGrciQ&t=1048s)** permanence on your tailnet.

**[17:30](https://youtube.com/watch?v=tqvvZhGrciQ&t=1050s)** So depending on your use case,

**[17:31](https://youtube.com/watch?v=tqvvZhGrciQ&t=1051s)** that may or may not be useful for you.

**[17:33](https://youtube.com/watch?v=tqvvZhGrciQ&t=1053s)** And again, just to verify what's going on here,

**[17:36](https://youtube.com/watch?v=tqvvZhGrciQ&t=1056s)** I want to do instead of doing it in the web browser this time,

**[17:40](https://youtube.com/watch?v=tqvvZhGrciQ&t=1060s)** I want to do it in a terminal session.

**[17:43](https://youtube.com/watch?v=tqvvZhGrciQ&t=1063s)** So I'm going to do a curl HTTP OAuth test

**[17:46](https://youtube.com/watch?v=tqvvZhGrciQ&t=1066s)** and you saw the web request flow by in the terminal underneath.

**[17:50](https://youtube.com/watch?v=tqvvZhGrciQ&t=1070s)** And then we get the the engine X landing page as well.

**[17:52](https://youtube.com/watch?v=tqvvZhGrciQ&t=1072s)** So there you go.

**[17:53](https://youtube.com/watch?v=tqvvZhGrciQ&t=1073s)** We've now added a node to our tailnet using an auth key

**[17:56](https://youtube.com/watch?v=tqvvZhGrciQ&t=1076s)** and also an OAuth client.

**[17:59](https://youtube.com/watch?v=tqvvZhGrciQ&t=1079s)** Now I promised you a bit of a deeper dive

**[18:02](https://youtube.com/watch?v=tqvvZhGrciQ&t=1082s)** as to how the Docker networking is actually connecting

**[18:04](https://youtube.com/watch?v=tqvvZhGrciQ&t=1084s)** everything together under the hood.

**[18:06](https://youtube.com/watch?v=tqvvZhGrciQ&t=1086s)** So we're going to dive a little bit into Linux kernel name spacing.

**[18:09](https://youtube.com/watch?v=tqvvZhGrciQ&t=1089s)** I promise it's not as intimidating as it sounds.

**[18:12](https://youtube.com/watch?v=tqvvZhGrciQ&t=1092s)** So when we create a container,

**[18:14](https://youtube.com/watch?v=tqvvZhGrciQ&t=1094s)** what we're doing effectively is creating a new name space

**[18:18](https://youtube.com/watch?v=tqvvZhGrciQ&t=1098s)** in the Linux kernel with a whole bunch of different things

**[18:21](https://youtube.com/watch?v=tqvvZhGrciQ&t=1101s)** that control where different resources live.

**[18:24](https://youtube.com/watch?v=tqvvZhGrciQ&t=1104s)** One of those name spaces that we create

**[18:26](https://youtube.com/watch?v=tqvvZhGrciQ&t=1106s)** is a networking name space that each container has its own

**[18:30](https://youtube.com/watch?v=tqvvZhGrciQ&t=1110s)** networking context.

**[18:33](https://youtube.com/watch?v=tqvvZhGrciQ&t=1113s)** When we add network mode to a specific container,

**[18:37](https://youtube.com/watch?v=tqvvZhGrciQ&t=1117s)** we can actually group two containers together

**[18:40](https://youtube.com/watch?v=tqvvZhGrciQ&t=1120s)** under the same name space.

**[18:42](https://youtube.com/watch?v=tqvvZhGrciQ&t=1122s)** So let me show you that in action.

**[18:44](https://youtube.com/watch?v=tqvvZhGrciQ&t=1124s)** So what I have over here is a Docker compose file.

**[18:46](https://youtube.com/watch?v=tqvvZhGrciQ&t=1126s)** It's basically the same as the one we had before.

**[18:49](https://youtube.com/watch?v=tqvvZhGrciQ&t=1129s)** It's got an engine X web server in it

**[18:51](https://youtube.com/watch?v=tqvvZhGrciQ&t=1131s)** as well as the tailscale container.

**[18:53](https://youtube.com/watch?v=tqvvZhGrciQ&t=1133s)** Now notice down here on line 22

**[18:55](https://youtube.com/watch?v=tqvvZhGrciQ&t=1135s)** that I've actually commented out network mode.

**[18:58](https://youtube.com/watch?v=tqvvZhGrciQ&t=1138s)** So when we bring these containers up,

**[19:00](https://youtube.com/watch?v=tqvvZhGrciQ&t=1140s)** what's actually going to happen under the hood?

**[19:02](https://youtube.com/watch?v=tqvvZhGrciQ&t=1142s)** Is it's going to create two networking name spaces

**[19:06](https://youtube.com/watch?v=tqvvZhGrciQ&t=1146s)** in the Linux kernel?

**[19:08](https://youtube.com/watch?v=tqvvZhGrciQ&t=1148s)** And we can just check that these two containers

**[19:10](https://youtube.com/watch?v=tqvvZhGrciQ&t=1150s)** are both running with a Docker PS hyphen A.

**[19:13](https://youtube.com/watch?v=tqvvZhGrciQ&t=1153s)** Let's suppose I want to find which ports

**[19:15](https://youtube.com/watch?v=tqvvZhGrciQ&t=1155s)** this engine X container is listening on internally.

**[19:18](https://youtube.com/watch?v=tqvvZhGrciQ&t=1158s)** Well, the first thing I might want to do

**[19:20](https://youtube.com/watch?v=tqvvZhGrciQ&t=1160s)** is grab a Docker exec.

**[19:22](https://youtube.com/watch?v=tqvvZhGrciQ&t=1162s)** Docker exec spawns a process inside the container,

**[19:25](https://youtube.com/watch?v=tqvvZhGrciQ&t=1165s)** a shell process,

**[19:26](https://youtube.com/watch?v=tqvvZhGrciQ&t=1166s)** and lets us attach to that,

**[19:27](https://youtube.com/watch?v=tqvvZhGrciQ&t=1167s)** assuming that that binary exists within the container.

**[19:30](https://youtube.com/watch?v=tqvvZhGrciQ&t=1170s)** So what I want to do here is do a Docker exec

**[19:33](https://youtube.com/watch?v=tqvvZhGrciQ&t=1173s)** then the name of the container in question,

**[19:35](https://youtube.com/watch?v=tqvvZhGrciQ&t=1175s)** which is engine X PID test one,

**[19:38](https://youtube.com/watch?v=tqvvZhGrciQ&t=1178s)** and then I'm going to do net stat minus ton ALP.

**[19:43](https://youtube.com/watch?v=tqvvZhGrciQ&t=1183s)** Ah, we run into our first issue.

**[19:47](https://youtube.com/watch?v=tqvvZhGrciQ&t=1187s)** And this is because images like engine X

**[19:49](https://youtube.com/watch?v=tqvvZhGrciQ&t=1189s)** are designed to be web servers.

**[19:51](https://youtube.com/watch?v=tqvvZhGrciQ&t=1191s)** They're not designed to be diagnostic tools.

**[19:53](https://youtube.com/watch?v=tqvvZhGrciQ&t=1193s)** And so a lot of containers strip out unnecessary binaries,

**[19:57](https://youtube.com/watch?v=tqvvZhGrciQ&t=1197s)** but using name spaces,

**[19:59](https://youtube.com/watch?v=tqvvZhGrciQ&t=1199s)** we can actually hop into the networking name space

**[20:03](https://youtube.com/watch?v=tqvvZhGrciQ&t=1203s)** or hop into the context of the networking name space,

**[20:06](https://youtube.com/watch?v=tqvvZhGrciQ&t=1206s)** using a tool called NSEnter.

**[20:09](https://youtube.com/watch?v=tqvvZhGrciQ&t=1209s)** Now this tool, it's really pretty cool, actually.

**[20:13](https://youtube.com/watch?v=tqvvZhGrciQ&t=1213s)** But what we can do is we can provide

**[20:15](https://youtube.com/watch?v=tqvvZhGrciQ&t=1215s)** a bunch of different contexts.

**[20:17](https://youtube.com/watch?v=tqvvZhGrciQ&t=1217s)** In here, for example,

**[20:18](https://youtube.com/watch?v=tqvvZhGrciQ&t=1218s)** we're going to use the dash N for net context.

**[20:21](https://youtube.com/watch?v=tqvvZhGrciQ&t=1221s)** And we need to grab the PID or the process ID

**[20:25](https://youtube.com/watch?v=tqvvZhGrciQ&t=1225s)** for the Docker container that we want to inspect.

**[20:28](https://youtube.com/watch?v=tqvvZhGrciQ&t=1228s)** So to do that,

**[20:29](https://youtube.com/watch?v=tqvvZhGrciQ&t=1229s)** we're going to use the Docker inspect command.

**[20:31](https://youtube.com/watch?v=tqvvZhGrciQ&t=1231s)** And I'm going to look for the PID of the container,

**[20:34](https://youtube.com/watch?v=tqvvZhGrciQ&t=1234s)** engine X PID test one,

**[20:36](https://youtube.com/watch?v=tqvvZhGrciQ&t=1236s)** which we can see here is 53166.

**[20:39](https://youtube.com/watch?v=tqvvZhGrciQ&t=1239s)** Then I'm going to use NSEnter.

**[20:41](https://youtube.com/watch?v=tqvvZhGrciQ&t=1241s)** I'm going to run it a pseudo

**[20:42](https://youtube.com/watch?v=tqvvZhGrciQ&t=1242s)** because I need root privileges to change

**[20:44](https://youtube.com/watch?v=tqvvZhGrciQ&t=1244s)** into a different name space.

**[20:45](https://youtube.com/watch?v=tqvvZhGrciQ&t=1245s)** Then I'm going to give it the target of 53166

**[20:49](https://youtube.com/watch?v=tqvvZhGrciQ&t=1249s)** because we're targeting the process ID

**[20:51](https://youtube.com/watch?v=tqvvZhGrciQ&t=1251s)** that owns or is part of that name space,

**[20:53](https://youtube.com/watch?v=tqvvZhGrciQ&t=1253s)** that owns the network name space.

**[20:55](https://youtube.com/watch?v=tqvvZhGrciQ&t=1255s)** And then I'm going to run the command

**[20:57](https://youtube.com/watch?v=tqvvZhGrciQ&t=1257s)** in the networking context,

**[20:59](https://youtube.com/watch?v=tqvvZhGrciQ&t=1259s)** Nets that TUN-ALP,

**[21:01](https://youtube.com/watch?v=tqvvZhGrciQ&t=1261s)** which if you recall,

**[21:02](https://youtube.com/watch?v=tqvvZhGrciQ&t=1262s)** is exactly the same command I tried to run before

**[21:05](https://youtube.com/watch?v=tqvvZhGrciQ&t=1265s)** with the Docker exec that didn't work.

**[21:07](https://youtube.com/watch?v=tqvvZhGrciQ&t=1267s)** And what we can see here is that within our engine X

**[21:10](https://youtube.com/watch?v=tqvvZhGrciQ&t=1270s)** container that we've got a couple of commands

**[21:12](https://youtube.com/watch?v=tqvvZhGrciQ&t=1272s)** running on IPv4 port 80 here,

**[21:14](https://youtube.com/watch?v=tqvvZhGrciQ&t=1274s)** as well as IPv6 on port 80 as well.

**[21:17](https://youtube.com/watch?v=tqvvZhGrciQ&t=1277s)** So let's just stop and think about what happened for a second.

**[21:20](https://youtube.com/watch?v=tqvvZhGrciQ&t=1280s)** I'm on my Linux host

**[21:22](https://youtube.com/watch?v=tqvvZhGrciQ&t=1282s)** and I changed into a different name space

**[21:25](https://youtube.com/watch?v=tqvvZhGrciQ&t=1285s)** using name space enter as the command.

**[21:28](https://youtube.com/watch?v=tqvvZhGrciQ&t=1288s)** And then I ran an arbitrary command

**[21:30](https://youtube.com/watch?v=tqvvZhGrciQ&t=1290s)** as if I was in the context of the container.

**[21:33](https://youtube.com/watch?v=tqvvZhGrciQ&t=1293s)** And so when we talk about containers,

**[21:35](https://youtube.com/watch?v=tqvvZhGrciQ&t=1295s)** that's what we're talking about,

**[21:37](https://youtube.com/watch?v=tqvvZhGrciQ&t=1297s)** is different contexts, different processes,

**[21:39](https://youtube.com/watch?v=tqvvZhGrciQ&t=1299s)** sliced up within the side of the Linux kernel in memory space.

**[21:43](https://youtube.com/watch?v=tqvvZhGrciQ&t=1303s)** But where things start to get really interesting

**[21:45](https://youtube.com/watch?v=tqvvZhGrciQ&t=1305s)** is when we start trying to stack the containers together

**[21:48](https://youtube.com/watch?v=tqvvZhGrciQ&t=1308s)** using network mode.

**[21:50](https://youtube.com/watch?v=tqvvZhGrciQ&t=1310s)** So over here in my Docker Compose file,

**[21:52](https://youtube.com/watch?v=tqvvZhGrciQ&t=1312s)** you can see that network mode is currently commented out.

**[21:55](https://youtube.com/watch?v=tqvvZhGrciQ&t=1315s)** What this means is that we're going to be creating

**[21:57](https://youtube.com/watch?v=tqvvZhGrciQ&t=1317s)** two different network name spaces

**[22:00](https://youtube.com/watch?v=tqvvZhGrciQ&t=1320s)** for these different containers, one each.

**[22:02](https://youtube.com/watch?v=tqvvZhGrciQ&t=1322s)** So let's do a Docker Compose up

**[22:05](https://youtube.com/watch?v=tqvvZhGrciQ&t=1325s)** and then use a couple of commands

**[22:07](https://youtube.com/watch?v=tqvvZhGrciQ&t=1327s)** to examine what's going on with the name spaces underneath.

**[22:10](https://youtube.com/watch?v=tqvvZhGrciQ&t=1330s)** So I've got an all in one command here

**[22:12](https://youtube.com/watch?v=tqvvZhGrciQ&t=1332s)** which is going to use NSN to once more.

**[22:15](https://youtube.com/watch?v=tqvvZhGrciQ&t=1335s)** And it's going to grab the PID.

**[22:17](https://youtube.com/watch?v=tqvvZhGrciQ&t=1337s)** See, it's going to use Docker inspectors we did before

**[22:19](https://youtube.com/watch?v=tqvvZhGrciQ&t=1339s)** to inspect the name space for TSNGNX test.

**[22:23](https://youtube.com/watch?v=tqvvZhGrciQ&t=1343s)** This is the tail scale container,

**[22:26](https://youtube.com/watch?v=tqvvZhGrciQ&t=1346s)** not the NGNX web server.

**[22:28](https://youtube.com/watch?v=tqvvZhGrciQ&t=1348s)** And you can see that my name space here,

**[22:32](https://youtube.com/watch?v=tqvvZhGrciQ&t=1352s)** the network name space for just this specific container,

**[22:35](https://youtube.com/watch?v=tqvvZhGrciQ&t=1355s)** only contains things pertaining to tail scale D.

**[22:38](https://youtube.com/watch?v=tqvvZhGrciQ&t=1358s)** So that must mean that this is the tail scale container.

**[22:41](https://youtube.com/watch?v=tqvvZhGrciQ&t=1361s)** And if I do the same thing again here

**[22:43](https://youtube.com/watch?v=tqvvZhGrciQ&t=1363s)** and I'm going to load instead of TSNGNX test,

**[22:46](https://youtube.com/watch?v=tqvvZhGrciQ&t=1366s)** I'm going to investigate NGNX PID test one.

**[22:50](https://youtube.com/watch?v=tqvvZhGrciQ&t=1370s)** We can see that we've got NGNX listening in its name space

**[22:53](https://youtube.com/watch?v=tqvvZhGrciQ&t=1373s)** inside its container.

**[22:55](https://youtube.com/watch?v=tqvvZhGrciQ&t=1375s)** So these two containers right now both have separate name spaces

**[22:59](https://youtube.com/watch?v=tqvvZhGrciQ&t=1379s)** within the Linux kernel with regards to networking.

**[23:02](https://youtube.com/watch?v=tqvvZhGrciQ&t=1382s)** Another way we can check this is to use Docker's built-in network tools.

**[23:06](https://youtube.com/watch?v=tqvvZhGrciQ&t=1386s)** So if we do Docker network LS,

**[23:09](https://youtube.com/watch?v=tqvvZhGrciQ&t=1389s)** this is going to show us all of the different Docker networks

**[23:12](https://youtube.com/watch?v=tqvvZhGrciQ&t=1392s)** that get created.

**[23:13](https://youtube.com/watch?v=tqvvZhGrciQ&t=1393s)** And by default, Docker Compose creates a new network per stack.

**[23:18](https://youtube.com/watch?v=tqvvZhGrciQ&t=1398s)** So what we have here is a stack called 0,3 NGNX example default.

**[23:23](https://youtube.com/watch?v=tqvvZhGrciQ&t=1403s)** So if I do a Docker network inspect of that network,

**[23:28](https://youtube.com/watch?v=tqvvZhGrciQ&t=1408s)** what we can see, and I'll just pipe it through to JQ.

**[23:31](https://youtube.com/watch?v=tqvvZhGrciQ&t=1411s)** So it looks pretty.

**[23:32](https://youtube.com/watch?v=tqvvZhGrciQ&t=1412s)** And what we can see here is there are two containers currently

**[23:35](https://youtube.com/watch?v=tqvvZhGrciQ&t=1415s)** on that Docker network.

**[23:36](https://youtube.com/watch?v=tqvvZhGrciQ&t=1416s)** They've both got their own IP address from the Docker bridge.

**[23:39](https://youtube.com/watch?v=tqvvZhGrciQ&t=1419s)** So this one, 0,3, this one, 0,2.

**[23:41](https://youtube.com/watch?v=tqvvZhGrciQ&t=1421s)** You can see the different names of the containers here as well.

**[23:44](https://youtube.com/watch?v=tqvvZhGrciQ&t=1424s)** And what this shows us is that these two containers are currently operating

**[23:49](https://youtube.com/watch?v=tqvvZhGrciQ&t=1429s)** as we would expect as isolated units.

**[23:52](https://youtube.com/watch?v=tqvvZhGrciQ&t=1432s)** Now, let's go ahead and uncomment network mode.

**[23:56](https://youtube.com/watch?v=tqvvZhGrciQ&t=1436s)** I'm going to recreate these containers and just watch what happens.

**[24:00](https://youtube.com/watch?v=tqvvZhGrciQ&t=1440s)** I'm going to run the same command again, Docker network inspect.

**[24:03](https://youtube.com/watch?v=tqvvZhGrciQ&t=1443s)** And suddenly, there is only one container showing up.

**[24:07](https://youtube.com/watch?v=tqvvZhGrciQ&t=1447s)** We can see it's TSNGNX test.

**[24:09](https://youtube.com/watch?v=tqvvZhGrciQ&t=1449s)** Well, this is exactly what we would expect

**[24:11](https://youtube.com/watch?v=tqvvZhGrciQ&t=1451s)** because the NGNX PID test one container,

**[24:15](https://youtube.com/watch?v=tqvvZhGrciQ&t=1455s)** we've given it access to the network namespace

**[24:18](https://youtube.com/watch?v=tqvvZhGrciQ&t=1458s)** of this TSNGNX test container.

**[24:20](https://youtube.com/watch?v=tqvvZhGrciQ&t=1460s)** So actually, what's happened is we've merged them together.

**[24:23](https://youtube.com/watch?v=tqvvZhGrciQ&t=1463s)** And we can prove this by looking inside the containers networking namespace.

**[24:26](https://youtube.com/watch?v=tqvvZhGrciQ&t=1466s)** So let's first examine the NGNX PID test one namespace and see what's going on.

**[24:32](https://youtube.com/watch?v=tqvvZhGrciQ&t=1472s)** And then let's examine the actual tail scale container upstream of that container.

**[24:38](https://youtube.com/watch?v=tqvvZhGrciQ&t=1478s)** What we've done is we've merged these two namespaces together in the kernel.

**[24:43](https://youtube.com/watch?v=tqvvZhGrciQ&t=1483s)** And you can see we've got the same processes running in both places.

**[24:47](https://youtube.com/watch?v=tqvvZhGrciQ&t=1487s)** So we've taken those two separate namespaces and merged them together

**[24:51](https://youtube.com/watch?v=tqvvZhGrciQ&t=1491s)** by using the network mode in the Docker Compose file.

**[24:55](https://youtube.com/watch?v=tqvvZhGrciQ&t=1495s)** So let's put all of this new knowledge together

**[24:59](https://youtube.com/watch?v=tqvvZhGrciQ&t=1499s)** and put a self-hosted recipe manager onto our tailnet.

**[25:02](https://youtube.com/watch?v=tqvvZhGrciQ&t=1502s)** I've got an app here called Mealy and another Docker Compose file,

**[25:06](https://youtube.com/watch?v=tqvvZhGrciQ&t=1506s)** which looks, again, suspiciously similar to the ones that we've been looking at throughout this video.

**[25:12](https://youtube.com/watch?v=tqvvZhGrciQ&t=1512s)** We've got our client auth key here.

**[25:15](https://youtube.com/watch?v=tqvvZhGrciQ&t=1515s)** We've got our tags.

**[25:16](https://youtube.com/watch?v=tqvvZhGrciQ&t=1516s)** There's a new one here called TS serve config,

**[25:19](https://youtube.com/watch?v=tqvvZhGrciQ&t=1519s)** which will come on to throughout this section.

**[25:22](https://youtube.com/watch?v=tqvvZhGrciQ&t=1522s)** And then we've mounted a couple of extra volumes.

**[25:24](https://youtube.com/watch?v=tqvvZhGrciQ&t=1524s)** We've got the config directory, which is where our tail scale serve configuration lives.

**[25:28](https://youtube.com/watch?v=tqvvZhGrciQ&t=1528s)** And then the actual application itself.

**[25:30](https://youtube.com/watch?v=tqvvZhGrciQ&t=1530s)** So we've got Mealy as an application here using Docker volumes to persist the data.

**[25:35](https://youtube.com/watch?v=tqvvZhGrciQ&t=1535s)** So let's bring this container up.

**[25:38](https://youtube.com/watch?v=tqvvZhGrciQ&t=1538s)** And it'll take a couple of seconds to start.

**[25:40](https://youtube.com/watch?v=tqvvZhGrciQ&t=1540s)** It uses g-unicorn under the hood.

**[25:42](https://youtube.com/watch?v=tqvvZhGrciQ&t=1542s)** And we can wait for it to come up on port 9000.

**[25:45](https://youtube.com/watch?v=tqvvZhGrciQ&t=1545s)** And this is important because what we were doing before with ngnex was on port 80.

**[25:50](https://youtube.com/watch?v=tqvvZhGrciQ&t=1550s)** So we didn't have to do anything to make web requests work.

**[25:53](https://youtube.com/watch?v=tqvvZhGrciQ&t=1553s)** We just, they just worked because it was on port 80.

**[25:56](https://youtube.com/watch?v=tqvvZhGrciQ&t=1556s)** This one, though, is on port 9000.

**[25:58](https://youtube.com/watch?v=tqvvZhGrciQ&t=1558s)** So if I go across here and go to Mealy port 9000,

**[26:03](https://youtube.com/watch?v=tqvvZhGrciQ&t=1563s)** we can see that's fine.

**[26:04](https://youtube.com/watch?v=tqvvZhGrciQ&t=1564s)** And it works just fine.

**[26:05](https://youtube.com/watch?v=tqvvZhGrciQ&t=1565s)** But it's on plain HTTP.

**[26:07](https://youtube.com/watch?v=tqvvZhGrciQ&t=1567s)** There's no TLS certificate or anything like that.

**[26:11](https://youtube.com/watch?v=tqvvZhGrciQ&t=1571s)** And I don't really want to have to remember port numbers.

**[26:15](https://youtube.com/watch?v=tqvvZhGrciQ&t=1575s)** And so this is where tail scale serve,

**[26:17](https://youtube.com/watch?v=tqvvZhGrciQ&t=1577s)** and in a minute, tail scale funnel, come into the equation.

**[26:21](https://youtube.com/watch?v=tqvvZhGrciQ&t=1581s)** Tail scale serve lets us provide a configuration file

**[26:24](https://youtube.com/watch?v=tqvvZhGrciQ&t=1584s)** that will tell basically a bit like a reverse proxy that will tell web requests where to go.

**[26:31](https://youtube.com/watch?v=tqvvZhGrciQ&t=1591s)** And so let's take a look at one.

**[26:32](https://youtube.com/watch?v=tqvvZhGrciQ&t=1592s)** I've got over here a sample JSON file.

**[26:35](https://youtube.com/watch?v=tqvvZhGrciQ&t=1595s)** We can see at the top, these first few lines refer to proxying TCP,

**[26:40](https://youtube.com/watch?v=tqvvZhGrciQ&t=1600s)** HTTPS traffic.

**[26:42](https://youtube.com/watch?v=tqvvZhGrciQ&t=1602s)** We want this.

**[26:43](https://youtube.com/watch?v=tqvvZhGrciQ&t=1603s)** This is a good thing.

**[26:44](https://youtube.com/watch?v=tqvvZhGrciQ&t=1604s)** Next up, we've got the web section.

**[26:46](https://youtube.com/watch?v=tqvvZhGrciQ&t=1606s)** This is what is basically acting like a reverse proxy.

**[26:49](https://youtube.com/watch?v=tqvvZhGrciQ&t=1609s)** So when I receive a request of Mealy dot velociraptor,

**[26:53](https://youtube.com/watch?v=tqvvZhGrciQ&t=1613s)** hi for noodlefish dot TS dot net on port 443 proxy that request under the hood

**[27:00](https://youtube.com/watch?v=tqvvZhGrciQ&t=1620s)** to local host port 9000.

**[27:03](https://youtube.com/watch?v=tqvvZhGrciQ&t=1623s)** Now remember that this is actually running inside the tail scale container.

**[27:08](https://youtube.com/watch?v=tqvvZhGrciQ&t=1628s)** But because we've done network mode and added that other container into the name space

**[27:13](https://youtube.com/watch?v=tqvvZhGrciQ&t=1633s)** of the tail scale container in the Linux kernel,

**[27:17](https://youtube.com/watch?v=tqvvZhGrciQ&t=1637s)** it's actually listening on port 9000 inside the tail scale container.

**[27:21](https://youtube.com/watch?v=tqvvZhGrciQ&t=1641s)** So that's how the local host part here works.

**[27:24](https://youtube.com/watch?v=tqvvZhGrciQ&t=1644s)** And then finally, I've got allow funnel set to false for right now.

**[27:28](https://youtube.com/watch?v=tqvvZhGrciQ&t=1648s)** Funnel would allow me to expose this application across the internet with no further configuration required

**[27:34](https://youtube.com/watch?v=tqvvZhGrciQ&t=1654s)** other than just changing this value to true.

**[27:36](https://youtube.com/watch?v=tqvvZhGrciQ&t=1656s)** So if he had friends and family in another country that weren't on your tail net for some reason,

**[27:41](https://youtube.com/watch?v=tqvvZhGrciQ&t=1661s)** changing this value from false to true would let them access this application

**[27:45](https://youtube.com/watch?v=tqvvZhGrciQ&t=1665s)** as if they were on your tail net.

**[27:48](https://youtube.com/watch?v=tqvvZhGrciQ&t=1668s)** Now remember that means it's also exposed to anybody on the internet.

**[27:52](https://youtube.com/watch?v=tqvvZhGrciQ&t=1672s)** So use this option with care.

**[27:54](https://youtube.com/watch?v=tqvvZhGrciQ&t=1674s)** The upshot of this configuration file is I can now go to Mealy dot velociraptor,

**[27:59](https://youtube.com/watch?v=tqvvZhGrciQ&t=1679s)** hi for noodlefish dot TS dot net.

**[28:02](https://youtube.com/watch?v=tqvvZhGrciQ&t=1682s)** And I don't have to worry about typing in port numbers or anything like that.

**[28:07](https://youtube.com/watch?v=tqvvZhGrciQ&t=1687s)** What you might actually notice in the terminal window at the bottom is that when I make this request,

**[28:12](https://youtube.com/watch?v=tqvvZhGrciQ&t=1692s)** it was actually requesting a certificate from let's encrypt.

**[28:15](https://youtube.com/watch?v=tqvvZhGrciQ&t=1695s)** So this website is exposed only on my tail net right now.

**[28:20](https://youtube.com/watch?v=tqvvZhGrciQ&t=1700s)** It's not on the public internet, but it's backed with a proper TLS certificate from let's encrypt.

**[28:26](https://youtube.com/watch?v=tqvvZhGrciQ&t=1706s)** So if I look at the certificate here, you can see it's a let's encrypt certificate.

**[28:30](https://youtube.com/watch?v=tqvvZhGrciQ&t=1710s)** And the whole purpose behind TLS really is to verify that you are actually talking to the web server

**[28:36](https://youtube.com/watch?v=tqvvZhGrciQ&t=1716s)** that you think you're talking to it verifies the ownership of that domain.

**[28:41](https://youtube.com/watch?v=tqvvZhGrciQ&t=1721s)** And so let's get logged in and have a little poke around and see what's what.

**[28:44](https://youtube.com/watch?v=tqvvZhGrciQ&t=1724s)** Just type in my password here.

**[28:46](https://youtube.com/watch?v=tqvvZhGrciQ&t=1726s)** And oh, yeah, I feel like I'm in the mood to bake some bread.

**[28:51](https://youtube.com/watch?v=tqvvZhGrciQ&t=1731s)** Don't you?

**[28:52](https://youtube.com/watch?v=tqvvZhGrciQ&t=1732s)** The easiest loaf you'll ever bake.

**[28:54](https://youtube.com/watch?v=tqvvZhGrciQ&t=1734s)** Well, that's fantastic.

**[28:55](https://youtube.com/watch?v=tqvvZhGrciQ&t=1735s)** We've got a self hosted recipe app on our tail net.

**[28:58](https://youtube.com/watch?v=tqvvZhGrciQ&t=1738s)** But if you noticed, if you were keen eyed hard coding things into a configuration file

**[29:03](https://youtube.com/watch?v=tqvvZhGrciQ&t=1743s)** is never going to be fun in the long term to manage at least.

**[29:07](https://youtube.com/watch?v=tqvvZhGrciQ&t=1747s)** And so what we've actually done is we've implemented under the hood.

**[29:11](https://youtube.com/watch?v=tqvvZhGrciQ&t=1751s)** A way to substitute the values in this file using this TS cert domain variable just here.

**[29:18](https://youtube.com/watch?v=tqvvZhGrciQ&t=1758s)** So if you put this into your configuration file, when tail scale starts up,

**[29:23](https://youtube.com/watch?v=tqvvZhGrciQ&t=1763s)** it will actually substitute the value of this variable for the domain of your containers tail net.

**[29:30](https://youtube.com/watch?v=tqvvZhGrciQ&t=1770s)** And we can verify this by hopping over to the container host itself.

**[29:33](https://youtube.com/watch?v=tqvvZhGrciQ&t=1773s)** So if I do a docker PSA and then look for a docker exec command in here.

**[29:39](https://youtube.com/watch?v=tqvvZhGrciQ&t=1779s)** So docker exec 0 3 B 1.

**[29:42](https://youtube.com/watch?v=tqvvZhGrciQ&t=1782s)** This is going to give me a shell inside the tail scale container itself.

**[29:46](https://youtube.com/watch?v=tqvvZhGrciQ&t=1786s)** What I can do is do a tail scale serve status.

**[29:50](https://youtube.com/watch?v=tqvvZhGrciQ&t=1790s)** This is going to show us that whenever we receive a request on the root of the domain.

**[29:54](https://youtube.com/watch?v=tqvvZhGrciQ&t=1794s)** So the slash is the root of the domain.

**[29:56](https://youtube.com/watch?v=tqvvZhGrciQ&t=1796s)** It's going to proxy local host port 9,000.

**[30:00](https://youtube.com/watch?v=tqvvZhGrciQ&t=1800s)** Now, if you're not a fan of typing out configuration files yourself, like I said,

**[30:04](https://youtube.com/watch?v=tqvvZhGrciQ&t=1804s)** you can do a dash JSON on the end and it will actually print out the whole file for you in exactly the right format.

**[30:11](https://youtube.com/watch?v=tqvvZhGrciQ&t=1811s)** If you need it to feed into the TS serve config environment variable that I showed you earlier,

**[30:17](https://youtube.com/watch?v=tqvvZhGrciQ&t=1817s)** it's really important for this configuration file that you mount a directory and not the specific file itself.

**[30:23](https://youtube.com/watch?v=tqvvZhGrciQ&t=1823s)** If you mount the file directly, it breaks the way that FS notify tells docker that the file has changed.

**[30:30](https://youtube.com/watch?v=tqvvZhGrciQ&t=1830s)** We haven't done that here, we've just mounted a directory so we're okay.

**[30:33](https://youtube.com/watch?v=tqvvZhGrciQ&t=1833s)** But just notice what happens when I change false to true, for example.

**[30:37](https://youtube.com/watch?v=tqvvZhGrciQ&t=1837s)** It creates a whole bunch of configuration on the tail scale side to now expose this application using tail scale funnel.

**[30:45](https://youtube.com/watch?v=tqvvZhGrciQ&t=1845s)** So anybody on the public internet could now access this application.

**[30:49](https://youtube.com/watch?v=tqvvZhGrciQ&t=1849s)** Evoila, we have a self hosted recipes app running natively on our tail net with a valid HTTPS certificate available both internally to tail net devices only.

**[31:01](https://youtube.com/watch?v=tqvvZhGrciQ&t=1861s)** And if you turned it on externally to other devices using tail scale funnel.

**[31:06](https://youtube.com/watch?v=tqvvZhGrciQ&t=1866s)** This approach scales to multiple containers and different operating systems as well.

**[31:11](https://youtube.com/watch?v=tqvvZhGrciQ&t=1871s)** Not only that, but you could also just think about it for a second.

**[31:14](https://youtube.com/watch?v=tqvvZhGrciQ&t=1874s)** You could run one container in your basement, you could run another one in digital ocean, for example.

**[31:20](https://youtube.com/watch?v=tqvvZhGrciQ&t=1880s)** And then have another one at your friend's house and have all of these different devices all talking to each other natively encrypted over tail scale.

**[31:29](https://youtube.com/watch?v=tqvvZhGrciQ&t=1889s)** If you're already a regular user of tail scale and docker, let us know down in the comments how you're using it so we can make it even better in the future.

**[31:36](https://youtube.com/watch?v=tqvvZhGrciQ&t=1896s)** Don't forget you can find all of the companion resources for this video in the description box down below.

**[31:41](https://youtube.com/watch?v=tqvvZhGrciQ&t=1901s)** It's just a blog post, the Git repo, various different K base articles.

**[31:45](https://youtube.com/watch?v=tqvvZhGrciQ&t=1905s)** They're all down there for you to use.

**[31:47](https://youtube.com/watch?v=tqvvZhGrciQ&t=1907s)** So until next time, thank you so much for watching. I've been Alex from tail scale.

---

*Automatically generated transcript. May contain errors.*
