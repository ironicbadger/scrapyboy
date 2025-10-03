import { defineCollection, z } from 'astro:content';

const transcripts = defineCollection({
  type: 'content',
  schema: z.object({
    video_id: z.string(),
    title: z.string(),
    description: z.string().optional(),
    channel_name: z.string(),
    channel_id: z.string(),
    published_at: z.string(),
    duration_seconds: z.number(),
    youtube_url: z.string(),
    thumbnail_url: z.string().optional(),
    transcribed_at: z.string(),
    transcription_method: z.string(),
    model_used: z.string(),
    language: z.string(),
    word_count: z.number().optional(),
    transcription_time_seconds: z.number().optional(),
  }),
});

export const collections = {
  transcripts,
};
