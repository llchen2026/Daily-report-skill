#!/bin/bash
# sync_from_github.sh — 从GitHub仓库同步skill最新版本
# 用法: bash sync_from_github.sh [target_skill_dir]
#   target_skill_dir 可选，默认为当前skill所在目录

set -e

REPO_URL="https://github.com/llchen2026/Daily-report-skill.git"
BRANCH="main"
SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"
SKILL_DIR="$(cd "$SCRIPT_DIR/.." && pwd)"
TARGET_DIR="${1:-$SKILL_DIR}"

echo "=== Skill GitHub 同步 ==="
echo "仓库: $REPO_URL ($BRANCH)"
echo "目标: $TARGET_DIR"
echo ""

# 创建临时目录
TMP_DIR=$(mktemp -d)
trap "rm -rf $TMP_DIR" EXIT

# Clone仓库
echo "[1/4] 拉取仓库..."
git clone --depth 1 --branch "$BRANCH" "$REPO_URL" "$TMP_DIR/repo"

# 检查是否有更新
echo "[2/4] 检查版本..."
NEW_HASH=$(cd "$TMP_DIR/repo" && git rev-parse HEAD)

# 查找已安装的版本hash记录
VERSION_FILE="$TARGET_DIR/.sync-version"
if [ -f "$VERSION_FILE" ]; then
    OLD_HASH=$(cat "$VERSION_FILE")
    if [ "$OLD_HASH" = "$NEW_HASH" ]; then
        echo "    已是最新版本 (commit: ${NEW_HASH:0:8})"
        echo "    无需更新。"
        exit 0
    fi
    echo "    发现新版本: ${OLD_HASH:0:8} -> ${NEW_HASH:0:8}"
else
    echo "    首次同步 (commit: ${NEW_HASH:0:8})"
fi

# 同步文件（排除.git目录和运行时产物）
echo "[3/4] 同步文件..."
rsync -av --delete \
    --exclude='.git' \
    --exclude='.gitignore' \
    --exclude='.sync-version' \
    --exclude='__pycache__' \
    --exclude='*.pyc' \
    --exclude='news-store/' \
    --exclude='*.jsonl' \
    --exclude='.akshare-data.json' \
    --exclude='oil-intel-dashboard-*' \
    "$TMP_DIR/repo/" "$TARGET_DIR/"

# 记录版本（写到TARGET_DIR，不受rsync --delete影响因为已exclude）
echo "$NEW_HASH" > "$TARGET_DIR/.sync-version"

echo "[4/4] 同步完成!"
echo ""
echo "    版本: ${NEW_HASH:0:8}"
echo "    时间: $(date '+%Y-%m-%d %H:%M:%S')"
echo ""
echo "如需查看变更日志:"
echo "  https://github.com/llchen2026/Daily-report-skill/commits/main"
