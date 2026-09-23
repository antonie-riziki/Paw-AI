# PAW AI (Predictive Animal Watch)

## Project Name
**PAW AI** (Predictive Animal Watch: AI-Powered System)

## Problem
Wildlife populations across Kenya and broader regions face severe threats due to poaching, habitat loss and fragmentation, human-wildlife conflicts, and illegal deforestation. Traditional conservation monitoring methods are often reactive, manual, and disconnected. Rangers lack real-time predictive insights to preempt threat activities, while local communities living adjacent to wildlife reserves often lack accessible, low-tech communication tools (e.g., SMS/USSD) to report incidents, access educational resources, or engage in conservation eco-tourism.

## Proposed Solution
PAW AI is a smart conservation platform designed to protect wildlife, prevent poaching, and foster community engagement using real-time data, machine learning, and multi-channel communication tools.

Key features and components include:
- **Predictive Threat & Movement Insights**: Aggregates GPS tracking, environmental data, and historical threat patterns to generate actionable alerts and optimize ranger patrol routes.
- **Interactive Mapping & Geo-Intelligence**: Visualizes national parks, reserves, sanctuaries, and forest corridors on an interactive map with key species metadata, entrance fees, and operational hours.
- **WildSnap AI Media Analysis**: Image and media identification system powered by Gemini 2.0 Flash to detect species, evaluate confidence, present conservation status, ecological roles, and threat levels from uploaded wildlife photos/videos.
- **PAW Bot (AI Wildlife Tour Guide & Conservation Expert)**: Streamlit-integrated chatbot leveraging generative AI to provide accurate, engaging wildlife information, park logistics, and guidelines.
- **Accessible Community Outreach**: Integration with Africa's Talking SMS, Voice, and USSD services to send alerts, OTPs, welcome messages, and engage local communities directly on mobile devices without relying on high-speed internet.

## Current Progress
- [x] **Core Streamlit Web Application Framework**: Structured multi-page application navigation including authentication (registration & sign-in), interactive mapping, WildSnap, and PAW Bot.
- [x] **Kenya Wildlife Mapping**: Interactive Folium map displaying national parks, game reserves, sanctuaries, and forests across Kenya with filtering and metadata tables.
- [x] **WildSnap Species Metadata Engine**: Functionality to analyze uploaded photos/videos using Google Gemini 2.0 Flash and output structured species identification and conservation reports.
- [x] **PAW Bot Assistant**: AI-powered conversational assistant tailored for Kenya wildlife guide topics and conservation inquiries.
- [x] **Africa's Talking Telecom Services**: Integration for SMS notifications, OTP generation/sending, and voice calls for user communication.
- [x] **Gemini Veo 3 Video Generation Experiments**: Script for generating promotional and instructional AI video content for community engagement.
