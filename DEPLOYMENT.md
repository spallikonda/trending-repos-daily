# 🚀 Quick Deployment Guide

## Step-by-Step Instructions to Get Your Site Live

### 1️⃣ Upload to GitHub

1. Create a new repository on GitHub:
   - Go to https://github.com/new
   - Name it: `github-trending-tracker` (or any name you prefer)
   - Make it **Public**
   - **Don't** initialize with README (we already have files)

2. Upload the files:
   ```bash
   cd github-trending-tracker
   git init
   git add .
   git commit -m "Initial commit"
   git branch -M main
   git remote add origin https://github.com/YOUR-USERNAME/github-trending-tracker.git
   git push -u origin main
   ```

   **OR** use GitHub's web interface:
   - Click "uploading an existing file"
   - Drag and drop all the folders and files

### 2️⃣ Enable GitHub Pages

1. Go to your repository on GitHub
2. Click **Settings** (top menu)
3. Click **Pages** (left sidebar)
4. Under "Build and deployment":
   - Source: **Deploy from a branch**
   - Branch: **main**
   - Folder: **/ (root)**
5. Click **Save**

🎉 Your site will be live in 1-2 minutes at:
`https://YOUR-USERNAME.github.io/github-trending-tracker/`

### 3️⃣ Enable Automatic Updates

1. Go to **Settings** → **Actions** → **General**
2. Scroll to "Workflow permissions"
3. Select **Read and write permissions**
4. Check ☑️ "Allow GitHub Actions to create and approve pull requests"
5. Click **Save**

### 4️⃣ Test the Automation

1. Go to the **Actions** tab
2. Click **Update Trending Repos** (left sidebar)
3. Click **Run workflow** (right side)
4. Select **main** branch
5. Click **Run workflow**

Wait 30-60 seconds, then refresh. You should see a successful run ✅

### 5️⃣ (Optional) Increase API Rate Limits

For better reliability:

1. Create a Personal Access Token:
   - Go to https://github.com/settings/tokens
   - Click **Generate new token (classic)**
   - Give it a name: "Trending Tracker"
   - **No scopes needed** (don't check any boxes)
   - Click **Generate token**
   - **Copy the token** (you won't see it again!)

2. Add the token to your repository:
   - Go to your repo **Settings** → **Secrets and variables** → **Actions**
   - Click **New repository secret**
   - Name: `GITHUB_TOKEN`
   - Value: Paste your token
   - Click **Add secret**

## 🎨 Customization Ideas

### Change Colors
Edit `index.html`, find this line and change the colors:
```css
background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
```

Try these:
- Ocean: `#2E3192 0%, #1BFFFF 100%`
- Sunset: `#FF512F 0%, #DD2476 100%`
- Forest: `#134E5E 0%, #71B280 100%`

### Change Update Time
Edit `.github/workflows/update-trending.yml`:
```yaml
- cron: '0 0 * * *'  # Midnight UTC
```

Examples:
- 6 AM UTC: `0 6 * * *`
- Every 12 hours: `0 */12 * * *`
- Weekdays only: `0 0 * * 1-5`

## 📞 Need Help?

- **Workflow not running?** Check Actions are enabled in Settings
- **Site not showing?** Wait 2-3 minutes after enabling Pages
- **Data not updating?** Check the Actions tab for error messages

## ✅ Checklist

- [ ] Repository created on GitHub
- [ ] All files uploaded
- [ ] GitHub Pages enabled
- [ ] Workflow permissions set
- [ ] First manual workflow run successful
- [ ] Site loads in browser
- [ ] (Optional) GitHub token added

## 🎉 You're Done!

Your GitHub Trending Tracker is now live and will update automatically every day!

Visit your site at: `https://YOUR-USERNAME.github.io/github-trending-tracker/`
