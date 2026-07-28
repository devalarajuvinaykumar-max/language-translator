/**
 * Translation Memory and Search History Engine (IndexedDB & LocalStorage)
 */

export class MemoryEngine {
  static STORAGE_KEY = "omni_translate_memory_v1";

  static getHistory() {
    try {
      const data = localStorage.getItem(this.STORAGE_KEY);
      return data ? JSON.parse(data) : [];
    } catch (e) {
      return [];
    }
  }

  static saveTranslation(item) {
    const history = this.getHistory();
    const newItem = {
      id: Date.now(),
      source_text: item.source_text,
      translated_text: item.translated_text,
      source_lang: item.source_lang,
      target_lang: item.target_lang,
      timestamp: new Date().toISOString(),
      bookmarked: false
    };
    history.unshift(newItem);
    // Keep top 100
    if (history.length > 100) history.pop();
    localStorage.setItem(this.STORAGE_KEY, JSON.stringify(history));
    return newItem;
  }

  static toggleBookmark(id) {
    const history = this.getHistory();
    const item = history.find(h => h.id === id);
    if (item) {
      item.bookmarked = !item.bookmarked;
      localStorage.setItem(this.STORAGE_KEY, JSON.stringify(history));
    }
    return history;
  }

  static exportAsJSON() {
    const data = JSON.stringify(this.getHistory(), null, 2);
    const blob = new Blob([data], { type: "application/json" });
    const url = URL.createObjectURL(blob);
    const a = document.createElement("a");
    a.href = url;
    a.download = `omni_translate_memory_${Date.now()}.json`;
    a.click();
  }
}
