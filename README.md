# 📊 GitHub Trending Tracker

A beautiful, automatically updating website that tracks the top 10 trending GitHub repositories daily. Built with vanilla JavaScript and hosted on GitHub Pages with automated daily updates via GitHub Actions.

![GitHub Trending Tracker](https://img.shields.io/badge/Status-Active-brightgreen)
![Auto Update](https://img.shields.io/badge/Updates-Daily-blue)
![License](https://img.shields.io/badge/License-MIT-yellow)

## ✨ Features

- **Daily Auto-Updates**: GitHub Actions automatically fetches trending repos every day at midnight UTC
- **Historical Data**: Browse trending repos from up to 90 days of history
- **Beautiful UI**: Modern, responsive design with smooth animations
- **Zero Backend**: Completely static site - just HTML, CSS, and JavaScript
- **Free Hosting**: Runs entirely on GitHub Pages at no cost
- **Mobile Friendly**: Fully responsive design works on all devices

## 🚀 Quick Start

### 1. Fork or Clone This Repository

```bash
git clone https://github.com/YOUR-USERNAME/github-trending-tracker.git
cd github-trending-tracker
```

### 2. Enable GitHub Pages

1. Go to your repository on GitHub
2. Click **Settings** → **Pages**
3. Under "Source", select **Deploy from a branch**
4. Select branch: `main` and folder: `/ (root)`
5. Click **Save**

Your site will be live at: `https://YOUR-USERNAME.github.io/github-trending-tracker/`

### 3. Enable GitHub Actions

1. Go to **Settings** → **Actions** → **General**
2. Under "Workflow permissions", select **Read and write permissions**
3. Click **Save**

The workflow will now run automatically every day at midnight UTC, or you can trigger it manually from the **Actions** tab.

## 📁 Project Structure

```
github-trending-tracker/
├── index.html                          # Main website file
├── data/
│   └── trending-history.json          # Historical trending data
├── scripts/
│   └── fetch-trending.py              # Python script to fetch trending repos
├── .github/
│   └── workflows/
│       └── update-trending.yml        # GitHub Actions workflow
└── README.md                          # This file
```

## 🔧 How It Works

### Daily Updates

1. **GitHub Actions** runs the workflow daily at 00:00 UTC
2. **Python script** fetches the top trending repositories using GitHub's API
3. **Data is saved** to `data/trending-history.json`
4. **Changes are committed** back to the repository
5. **GitHub Pages** automatically deploys the update

### Frontend

- Pure **vanilla JavaScript** - no frameworks needed
- Reads from `trending-history.json` to display data
- Two views: Today's trending and historical data
- Responsive design using modern CSS Grid and Flexbox

## 🎨 Customization

### Change Update Frequency

Edit `.github/workflows/update-trending.yml`:

```yaml
on:
  schedule:
    - cron: '0 0 * * *'  # Change this cron expression
```

Examples:
- Every 6 hours: `0 */6 * * *`
- Twice daily: `0 0,12 * * *`
- Weekly: `0 0 * * 0`

### Change Number of Repos

Edit `scripts/fetch-trending.py`:

```python
repos = fetch_trending_from_github_trending()[:10]  # Change 10 to desired number
```

### Modify Colors

Edit the CSS in `index.html`:

```css
background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
```

## 🔑 GitHub API Rate Limits

The script uses the public GitHub API which has rate limits:

- **Unauthenticated**: 60 requests/hour
- **Authenticated**: 5,000 requests/hour

To use authenticated requests (recommended):

1. Create a GitHub Personal Access Token (no special permissions needed)
2. Go to your repo **Settings** → **Secrets and variables** → **Actions**
3. Create a new secret named `GITHUB_TOKEN` with your token

The workflow will automatically use this token if available.

## 📊 Data Management

- Historical data is kept for **90 days**
- Older data is automatically pruned
- Data file is stored in JSON format
- Easy to export or analyze

## 🛠️ Manual Trigger

You can manually trigger an update:

1. Go to **Actions** tab
2. Select **Update Trending Repos**
3. Click **Run workflow**

## 🐛 Troubleshooting

### Workflow Not Running

- Check that Actions are enabled in repository settings
- Verify workflow permissions (read and write)
- Check Actions tab for error logs

### Data Not Updating

- Ensure the workflow ran successfully (check Actions tab)
- Verify the Python script has no errors
- Check if API rate limits were exceeded

### Site Not Displaying

- Verify GitHub Pages is enabled
- Check that `index.html` is in the root directory
- Look for JavaScript errors in browser console

## 📈 Future Enhancements

Possible features to add:

- [ ] Charts showing trending history over time
- [ ] Filter by programming language
- [ ] Search functionality
- [ ] Export data to CSV
- [ ] Dark mode toggle
- [ ] Email notifications for specific repos

## 📝 License

MIT License - feel free to use this project however you'd like!

## 🤝 Contributing

Contributions are welcome! Feel free to:

- Report bugs
- Suggest features
- Submit pull requests

## 🌟 Acknowledgments

- Data from GitHub's API and trending repositories
- Inspired by the need for historical trending data
- Built with ❤️ and vanilla JavaScript

---

**Made with ❤️ by [Your Name]**

If you find this useful, consider giving it a ⭐ on GitHub!
