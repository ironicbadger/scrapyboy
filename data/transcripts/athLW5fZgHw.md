---
video_id: "athLW5fZgHw"
title: "How to monitor your Tailscale nodes with Prometheus"
description: "What are the nodes in your tailnet up to? Do you know? 

In today's video, Alex walks you through the process of setting up a monitoring system for your tailnet using Prometheus and the brand new Tail..."
channel_name: "Tailscale"
channel_id: "UCcdv38QxPjSMqbt5ffLhJLA"
published_at: "2025-02-10"
duration_seconds: 711
youtube_url: "https://www.youtube.com/watch?v=athLW5fZgHw"
thumbnail_url: "https://i.ytimg.com/vi_webp/athLW5fZgHw/maxresdefault.webp"

# Transcription metadata
transcribed_at: "2025-10-03T18:11:49.835320"
transcription_method: "cpu"
model_used: "base"
language: "en"
word_count: 2180
transcription_time_seconds: 19.3
---

# How to monitor your Tailscale nodes with Prometheus

**[00:00](https://youtube.com/watch?v=athLW5fZgHw&t=0s)** Hi, I'm Alex from Tailscale, and in today's video, we're going to look at Prometheus and the new Tailscale client metrics feature. This allows you to expose a bunch of metrics from your Tailscale clients and scrape those statistics into Prometheus. So in today's video, I'm going to show you the basics of setting up Prometheus with a Grafana dashboard and just sort of talk through the basics of what you can do with this new client metrics feature with Tailscale. Now, I'm going to put a link to this blog post in the description down below, but a colleague of mine, Parker, has written

**[00:31](https://youtube.com/watch?v=athLW5fZgHw&t=31s)** a wonderful blog post going into more details on this feature. Of course, you can find a link in our documentation available here in the description as well. But the short version of what we're going to show today is this. Doesn't look very glamorous, does it? Let me make that a bit bigger for you. Essentially, what this does, this is being loaded from a Tailscale node. In this case, Prometheus is running inside of a Docker container, and then I'm scraping the metrics from inside of that container and showing them to you in this web page.

**[01:01](https://youtube.com/watch?v=athLW5fZgHw&t=61s)** So as I refresh this page, you'll see that things like the direct IPv4 package total goes up inbound, as does the outbound, you know, all this kind of stuff. So as I refresh that page, that changes. And so what happens in the background, Prometheus scrapes or has a bunch of jobs configured into it and scrapes these metrics into its database, a time series database. What Prometheus then does is it exposes a bunch of levers to a tool called Grafana, which I'll show you.

**[01:31](https://youtube.com/watch?v=athLW5fZgHw&t=91s)** Right here, which allows us to visualize what's going on, what's being scraped. So you can see here that I had a huge load spike at around about 345 in the afternoon. So what this can do as a Tailscale administrator is allow you to spot patterns and trends in your tailnet traffic. Let's say you've got a specific subnet router that's dealing with a ton of traffic and your users are complaining that things are taking longer than usual.

**[01:58](https://youtube.com/watch?v=athLW5fZgHw&t=118s)** Well, now you can monitor this kind of stuff using Prometheus and alert on it based on alert manager, which is a plug in for Prometheus that has a bunch of thresholds in it that says, hey, this this value has been above your threshold for X number of minutes.

**[02:13](https://youtube.com/watch?v=athLW5fZgHw&t=133s)** I'm going to send you an alert you should probably go take a look at this. So that's the basics of what the client metrics does essentially we expose a bunch of text records.

**[02:23](https://youtube.com/watch?v=athLW5fZgHw&t=143s)** Prometheus then reaches out scrapes those records puts them into its time series database. And then Grafana goes and queries that time series database and makes a pretty dashboard that's human readable.

**[02:36](https://youtube.com/watch?v=athLW5fZgHw&t=156s)** So with all of those basics out of the way, let's cover the basics of setting it up on an existing tailscale node.

**[02:43](https://youtube.com/watch?v=athLW5fZgHw&t=163s)** Now you can see here I've got a Docker compose file. This is how I'm running Grafana. It's just a node on my tailnet. I've shown you many times on this channel.

**[02:51](https://youtube.com/watch?v=athLW5fZgHw&t=171s)** How to do a sidecar Docker proxy for tailscale for a specific application. That's all I'm doing here. I'll put a link to the Docker video deep dive up here for those of you curious to find out a bit more about Docker and tailscale.

**[03:03](https://youtube.com/watch?v=athLW5fZgHw&t=183s)** I'm also doing the same thing with Prometheus and this is important because if you think about what's happening in terms of a network layer,

**[03:10](https://youtube.com/watch?v=athLW5fZgHw&t=190s)** Prometheus wants to reach out to every node on your tailnet and grab those metrics. And unless you put Prometheus on the tailnet or the node that's hosting Prometheus on the tailnet,

**[03:22](https://youtube.com/watch?v=athLW5fZgHw&t=202s)** it's not going to have the network roots available to it to do that. So it's really is less vitally put Grafana on the tailnet.

**[03:30](https://youtube.com/watch?v=athLW5fZgHw&t=210s)** Although that's what I did here, but it's pretty vital that you put Prometheus on the tailnet itself. Otherwise, it just won't have the ability to go and scrape that data for you remotely.

**[03:42](https://youtube.com/watch?v=athLW5fZgHw&t=222s)** Now the other thing that you want to pay attention to is your Prometheus YAML file. I'll put all of this stuff by the way as always as a GitHub repo link down in the description down below.

**[03:53](https://youtube.com/watch?v=athLW5fZgHw&t=233s)** For all of these code snippets, you can see here on the left every video that I make that needs code snippets just goes in this repo.

**[03:59](https://youtube.com/watch?v=athLW5fZgHw&t=239s)** So if you're ever wondering where to find all of this fantastically written code, it's down there.

**[04:05](https://youtube.com/watch?v=athLW5fZgHw&t=245s)** So Prometheus.YAML, this is essentially the secret source. This is what configures Prometheus to scrape different targets, different configurations.

**[04:14](https://youtube.com/watch?v=athLW5fZgHw&t=254s)** And these are the different jobs that Prometheus is going to execute.

**[04:18](https://youtube.com/watch?v=athLW5fZgHw&t=258s)** There's a bunch of stuff here. We don't really need to worry about the scrape interval 15 seconds. Yada, yada, yada.

**[04:23](https://youtube.com/watch?v=athLW5fZgHw&t=263s)** A bunch of alert rules, which I haven't actually set up, so I might just delete that in future.

**[04:28](https://youtube.com/watch?v=athLW5fZgHw&t=268s)** But what we're going to pay attention to today are these scrape configs here.

**[04:32](https://youtube.com/watch?v=athLW5fZgHw&t=272s)** And you can see they're pretty straightforward. The first job, Prometheus is scraping itself.

**[04:38](https://youtube.com/watch?v=athLW5fZgHw&t=278s)** So you can actually use Prometheus to monitor Prometheus. If you trust it, it's a little bit inception, but there you go.

**[04:44](https://youtube.com/watch?v=athLW5fZgHw&t=284s)** We can also use the Prometheus node exporter, which is also configured in the YAML file, by the way.

**[04:50](https://youtube.com/watch?v=athLW5fZgHw&t=290s)** Let me just put this alongside over here. You can see here I've got the Prometheus node exporter.

**[04:56](https://youtube.com/watch?v=athLW5fZgHw&t=296s)** Now, this is what you can use to monitor a specific host itself as opposed to using the tail scale metrics exposition feature.

**[05:04](https://youtube.com/watch?v=athLW5fZgHw&t=304s)** So this node exporter is something made by Prometheus that you can just run on your system.

**[05:09](https://youtube.com/watch?v=athLW5fZgHw&t=309s)** And that's running on port 9100. Again, that's not specific to tail scale.

**[05:14](https://youtube.com/watch?v=athLW5fZgHw&t=314s)** And then see advisor is just a container advisor, a container monitoring tool.

**[05:19](https://youtube.com/watch?v=athLW5fZgHw&t=319s)** It does pretty much the same thing as node exporter, but it's designed specifically for containers.

**[05:24](https://youtube.com/watch?v=athLW5fZgHw&t=324s)** What we want to pay attention to is our Prometheus container.

**[05:29](https://youtube.com/watch?v=athLW5fZgHw&t=329s)** So I've created here this little job that's going to scrape a target on port 9000 and two.

**[05:36](https://youtube.com/watch?v=athLW5fZgHw&t=336s)** So if we go to port 9000 and two on our Prometheus host, we can see that we have the tail scale metrics exposed.

**[05:43](https://youtube.com/watch?v=athLW5fZgHw&t=343s)** So this scrape job in the Prometheus YAML file is going to scrape specifically tail scale metrics.

**[05:49](https://youtube.com/watch?v=athLW5fZgHw&t=349s)** We can use this identifier of prom container. We can use this identifier in our Prometheus queries.

**[05:56](https://youtube.com/watch?v=athLW5fZgHw&t=356s)** So if we do this, some by instance, tail scale inbound by its path direct IPv4 for the job prom container.

**[06:05](https://youtube.com/watch?v=athLW5fZgHw&t=365s)** We can limit our query to just results that were scraped by that specific job.

**[06:11](https://youtube.com/watch?v=athLW5fZgHw&t=371s)** And so where that becomes interesting is let's say you want to start monitoring multiple of your tail scale nodes.

**[06:17](https://youtube.com/watch?v=athLW5fZgHw&t=377s)** You can just add another option in here and call this prom container to.

**[06:21](https://youtube.com/watch?v=athLW5fZgHw&t=381s)** And obviously you'd update the host name to say, you know, remote node number 73, whatever the host name is in your tail net.

**[06:29](https://youtube.com/watch?v=athLW5fZgHw&t=389s)** And that's what this is, by the way, this is the host name of Prometheus on my tail net.

**[06:33](https://youtube.com/watch?v=athLW5fZgHw&t=393s)** So the DNS resolves just fine because that's the way tail scale works.

**[06:37](https://youtube.com/watch?v=athLW5fZgHw&t=397s)** And again, you would do the same thing here.

**[06:39](https://youtube.com/watch?v=athLW5fZgHw&t=399s)** Just make sure that you're targeting the remote metrics URL and you should be good to go.

**[06:44](https://youtube.com/watch?v=athLW5fZgHw&t=404s)** And you can query things based off that unique identifier of the job name right here.

**[06:49](https://youtube.com/watch?v=athLW5fZgHw&t=409s)** So if I now execute this query, you can see that this number 29852612 should broadly match 29.

**[06:57](https://youtube.com/watch?v=athLW5fZgHw&t=417s)** There you go direct IPv4 close enough.

**[07:00](https://youtube.com/watch?v=athLW5fZgHw&t=420s)** OK, so once everything set up, it's dead easy.

**[07:04](https://youtube.com/watch?v=athLW5fZgHw&t=424s)** But the tricky part is trying to figure out how to switch on.

**[07:07](https://youtube.com/watch?v=athLW5fZgHw&t=427s)** No, it's not even that tricky, but trying to switch on the metrics monitoring in and of itself with the container to piece of cake.

**[07:15](https://youtube.com/watch?v=athLW5fZgHw&t=435s)** We just add one environment variable of TS enable metrics equals true.

**[07:20](https://youtube.com/watch?v=athLW5fZgHw&t=440s)** And that exposes on the internal port 9002 for the container.

**[07:24](https://youtube.com/watch?v=athLW5fZgHw&t=444s)** That exposes the metrics on that endpoint.

**[07:27](https://youtube.com/watch?v=athLW5fZgHw&t=447s)** But what if you're running just a bog standard Linux node like I am here?

**[07:31](https://youtube.com/watch?v=athLW5fZgHw&t=451s)** So I'm on a proxmox node here.

**[07:33](https://youtube.com/watch?v=athLW5fZgHw&t=453s)** This is just Clarkson part of my standard demo cluster.

**[07:37](https://youtube.com/watch?v=athLW5fZgHw&t=457s)** And you can see there's what half a dozen nodes in my tail net right here.

**[07:41](https://youtube.com/watch?v=athLW5fZgHw&t=461s)** And I'm going to do something.

**[07:42](https://youtube.com/watch?v=athLW5fZgHw&t=462s)** I'm going to just do tail scale set dash dash web client.

**[07:47](https://youtube.com/watch?v=athLW5fZgHw&t=467s)** Now if you've never seen the web client before, it's actually pretty cool.

**[07:50](https://youtube.com/watch?v=athLW5fZgHw&t=470s)** So I'm going to copy this address here 100.126 and then the ports 52.52.

**[07:57](https://youtube.com/watch?v=athLW5fZgHw&t=477s)** And you can see I get a whole bunch of information about my node.

**[08:00](https://youtube.com/watch?v=athLW5fZgHw&t=480s)** You can I can see the fact that tail scale ssh is running.

**[08:03](https://youtube.com/watch?v=athLW5fZgHw&t=483s)** I can see the fact that it's running as an exit node as a bunch of other information here too.

**[08:08](https://youtube.com/watch?v=athLW5fZgHw&t=488s)** But bet you didn't know this.

**[08:10](https://youtube.com/watch?v=athLW5fZgHw&t=490s)** If you do slash metrics, you can actually access the Prometheus compatible scrapable metrics here too.

**[08:18](https://youtube.com/watch?v=athLW5fZgHw&t=498s)** So if I wanted to add this node into my Prometheus configuration,

**[08:21](https://youtube.com/watch?v=athLW5fZgHw&t=501s)** I'd copy this address after I'd enabled the web client on a node and go to VS code over here.

**[08:29](https://youtube.com/watch?v=athLW5fZgHw&t=509s)** Modify my Prometheus YAML and just simply drop that in there.

**[08:33](https://youtube.com/watch?v=athLW5fZgHw&t=513s)** I don't think we need the HTTP.

**[08:35](https://youtube.com/watch?v=athLW5fZgHw&t=515s)** So I'll just remove that.

**[08:37](https://youtube.com/watch?v=athLW5fZgHw&t=517s)** And there you go.

**[08:38](https://youtube.com/watch?v=athLW5fZgHw&t=518s)** You can either use the 100.ip address or the host name of the node itself.

**[08:42](https://youtube.com/watch?v=athLW5fZgHw&t=522s)** So I could replace this 100 pts here with Clarkson if I wanted to.

**[08:48](https://youtube.com/watch?v=athLW5fZgHw&t=528s)** And that's it.

**[08:49](https://youtube.com/watch?v=athLW5fZgHw&t=529s)** That's how you add a new node to Prometheus.

**[08:52](https://youtube.com/watch?v=athLW5fZgHw&t=532s)** So if you're in the middle of a debugging session and you would like access to this information,

**[08:56](https://youtube.com/watch?v=athLW5fZgHw&t=536s)** you don't have to worry about Prometheus or enabling web clients or any of that other complexity.

**[09:01](https://youtube.com/watch?v=athLW5fZgHw&t=541s)** You can actually just type tail scale metrics and it will print it out for you

**[09:05](https://youtube.com/watch?v=athLW5fZgHw&t=545s)** in a nice human readable format-ish if you're a machine anyway.

**[09:10](https://youtube.com/watch?v=athLW5fZgHw&t=550s)** And you can take a look at this information here.

**[09:12](https://youtube.com/watch?v=athLW5fZgHw&t=552s)** Some interesting things to note, by the way.

**[09:15](https://youtube.com/watch?v=athLW5fZgHw&t=555s)** You can see the number of packets that get sent through a DURP server.

**[09:17](https://youtube.com/watch?v=athLW5fZgHw&t=557s)** So this can be useful to help you establish whether a node is being sent through a relay proxy or not.

**[09:23](https://youtube.com/watch?v=athLW5fZgHw&t=563s)** You can see whether direct packets are coming in, whether it's IPv4 or V6.

**[09:27](https://youtube.com/watch?v=athLW5fZgHw&t=567s)** A bunch of other useful information in this screen too.

**[09:31](https://youtube.com/watch?v=athLW5fZgHw&t=571s)** Now, before we get out of here, I've got one more little thing I want to show you.

**[09:34](https://youtube.com/watch?v=athLW5fZgHw&t=574s)** And this is how to generate some fake load that might be useful for testing for a video or for,

**[09:41](https://youtube.com/watch?v=athLW5fZgHw&t=581s)** you know, show your colleagues that things are working in a certain way.

**[09:44](https://youtube.com/watch?v=athLW5fZgHw&t=584s)** It's nothing fancy.

**[09:45](https://youtube.com/watch?v=athLW5fZgHw&t=585s)** It's just a script I had AI help me write.

**[09:47](https://youtube.com/watch?v=athLW5fZgHw&t=587s)** My friend Claude helped me write this one.

**[09:49](https://youtube.com/watch?v=athLW5fZgHw&t=589s)** It's probably rubbish code, but it does what I need to for this video.

**[09:54](https://youtube.com/watch?v=athLW5fZgHw&t=594s)** So there's a file in the GitHub repo down below called highload.py.

**[10:00](https://youtube.com/watch?v=athLW5fZgHw&t=600s)** And we can use that inside of a container to generate some load on our remote systems.

**[10:06](https://youtube.com/watch?v=athLW5fZgHw&t=606s)** So if I copy this Docker command here, I am going to change into the load gen directory,

**[10:13](https://youtube.com/watch?v=athLW5fZgHw&t=613s)** paste the Docker run command, and now it's going to generate concurrent load using up to 10 workers.

**[10:20](https://youtube.com/watch?v=athLW5fZgHw&t=620s)** It's just a basic Python script.

**[10:23](https://youtube.com/watch?v=athLW5fZgHw&t=623s)** Now, if I jump back to Grafana and go to last five minutes, I think will be good.

**[10:29](https://youtube.com/watch?v=athLW5fZgHw&t=629s)** You can see I was doing a little bit of testing before I started recording.

**[10:33](https://youtube.com/watch?v=athLW5fZgHw&t=633s)** If I refresh this every five seconds, there you go.

**[10:35](https://youtube.com/watch?v=athLW5fZgHw&t=635s)** You can now see that just just by virtue of doing some of this stuff in the background,

**[10:40](https://youtube.com/watch?v=athLW5fZgHw&t=640s)** that Grafana is now picking up using the Prometheus metrics that are being changed.

**[10:45](https://youtube.com/watch?v=athLW5fZgHw&t=645s)** If we refresh this page, we can see in real time these numbers are going up, up, up.

**[10:50](https://youtube.com/watch?v=athLW5fZgHw&t=650s)** And that's really simply that's all Grafana is doing.

**[10:54](https://youtube.com/watch?v=athLW5fZgHw&t=654s)** So this dashboard was configured using JSON.

**[10:59](https://youtube.com/watch?v=athLW5fZgHw&t=659s)** So if I go into settings here, JSON model.

**[11:01](https://youtube.com/watch?v=athLW5fZgHw&t=661s)** Again, this will be in the description down below.

**[11:04](https://youtube.com/watch?v=athLW5fZgHw&t=664s)** If you wanted to build a dashboard for your tailnet, you could quite easily have each node

**[11:08](https://youtube.com/watch?v=athLW5fZgHw&t=668s)** and the amount of traffic going through each node put into a Grafana dashboard

**[11:12](https://youtube.com/watch?v=athLW5fZgHw&t=672s)** and outbound packets per node and you can get pretty fancy with Grafana.

**[11:17](https://youtube.com/watch?v=athLW5fZgHw&t=677s)** So essentially, I think that's probably all you need to know about tail scales,

**[11:20](https://youtube.com/watch?v=athLW5fZgHw&t=680s)** new client metrics feature.

**[11:22](https://youtube.com/watch?v=athLW5fZgHw&t=682s)** If you're looking to bring tail scale to work, you can go to tailscale.com slash BTW

**[11:26](https://youtube.com/watch?v=athLW5fZgHw&t=686s)** to learn more about how some of our customers have gone ahead and made the switch to tail scale.

**[11:31](https://youtube.com/watch?v=athLW5fZgHw&t=691s)** And until next time, thank you very much for watching.

**[11:33](https://youtube.com/watch?v=athLW5fZgHw&t=693s)** I've been Alex from tail scale.

---

*Automatically generated transcript. May contain errors.*
