from youtube_transcript_api import YouTubeTranscriptApi
from youtube_transcript_api._transcripts import TranscriptList

def get_transcript(youtube_url):
    if "v=" in youtube_url:
        video_id = youtube_url.split("v=")[1].split("&")[0]
    else:
        video_id = youtube_url.split("/")[-1]
    
    ytt_api = YouTubeTranscriptApi()
    transcript_list = ytt_api.list(video_id)
    
    # Find any available transcript and fetch it
    for transcript in transcript_list:
        fetched = transcript.fetch()
        full_text = " ".join([t.text for t in fetched])
        return full_text