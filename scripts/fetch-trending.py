#!/usr/bin/env python3
"""
Fetch trending GitHub repositories and update the historical data.
"""

import json
import os
from datetime import datetime
from pathlib import Path
import requests
import time

def fetch_trending_repos(max_repos=10):
    """
    Fetch trending repositories from GitHub.
    Uses the GitHub API to search for repositories sorted by stars.
    """
    print("Fetching trending repositories...")
    
    # Get repositories created in the last 7 days, sorted by stars
    # This gives us trending repos
    today = datetime.now().strftime('%Y-%m-%d')
    week_ago = datetime.now().replace(day=datetime.now().day-7).strftime('%Y-%m-%d')
    
    # GitHub API endpoint
    url = "https://api.github.com/search/repositories"
    
    params = {
        'q': f'created:>{week_ago}',
        'sort': 'stars',
        'order': 'desc',
        'per_page': max_repos
    }
    
    headers = {
        'Accept': 'application/vnd.github.v3+json',
    }
    
    # Add token if available (for higher rate limits)
    github_token = os.environ.get('GITHUB_TOKEN')
    if github_token:
        headers['Authorization'] = f'token {github_token}'
    
    try:
        response = requests.get(url, params=params, headers=headers, timeout=30)
        response.raise_for_status()
        data = response.json()
        
        repos = []
        for item in data.get('items', [])[:max_repos]:
            repo = {
                'name': item['full_name'],
                'url': item['html_url'],
                'description': item['description'],
                'stars': item['stargazers_count'],
                'forks': item['forks_count'],
                'language': item['language'],
                'stars_today': item.get('stargazers_count', 0)  # Approximate
            }
            repos.append(repo)
            
        print(f"Successfully fetched {len(repos)} repositories")
        return repos
        
    except requests.exceptions.RequestException as e:
        print(f"Error fetching data: {e}")
        return []

def fetch_trending_from_github_trending():
    """
    Alternative method: scrape from github-trending-repos API
    This provides actual trending repos for today
    """
    print("Fetching from trending API...")
    
    url = "https://api.gitterapp.com/repositories"
    
    try:
        response = requests.get(url, timeout=30)
        response.raise_for_status()
        data = response.json()
        
        repos = []
        for item in data[:10]:
            repo = {
                'name': item['fullName'],
                'url': item['url'],
                'description': item.get('description', ''),
                'stars': item.get('stars', 0),
                'forks': item.get('forks', 0),
                'language': item.get('language', ''),
                'stars_today': item.get('todayStars', 0)
            }
            repos.append(repo)
            
        print(f"Successfully fetched {len(repos)} trending repositories")
        return repos
        
    except Exception as e:
        print(f"Error with trending API: {e}")
        return None

def update_history(repos):
    """
    Update the trending history JSON file.
    """
    data_dir = Path(__file__).parent.parent / 'data'
    data_dir.mkdir(exist_ok=True)
    
    history_file = data_dir / 'trending-history.json'
    
    # Load existing history
    if history_file.exists():
        with open(history_file, 'r', encoding='utf-8') as f:
            history = json.load(f)
    else:
        history = {}
    
    # Add today's data
    today = datetime.now().strftime('%Y-%m-%d')
    history[today] = repos
    
    # Keep only last 90 days of history
    sorted_dates = sorted(history.keys(), reverse=True)
    if len(sorted_dates) > 90:
        for old_date in sorted_dates[90:]:
            del history[old_date]
    
    # Save updated history
    with open(history_file, 'w', encoding='utf-8') as f:
        json.dump(history, f, indent=2, ensure_ascii=False)
    
    print(f"Updated history file with {len(repos)} repositories for {today}")
    print(f"Total days in history: {len(history)}")

def main():
    """Main execution function."""
    
    # Try the trending API first (more accurate)
    repos = fetch_trending_from_github_trending()
    
    # Fallback to search API if trending API fails
    if not repos or len(repos) == 0:
        print("Falling back to search API...")
        repos = fetch_trending_repos(max_repos=10)
    
    if repos:
        update_history(repos)
        print("✅ Successfully updated trending repositories!")
    else:
        print("❌ No repositories fetched. Skipping update.")
        exit(1)

if __name__ == '__main__':
    main()
