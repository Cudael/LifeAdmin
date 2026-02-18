/**
 * Shared composable for item expiration status logic.
 * Eliminates duplicated daysLeft / getStatus code across
 * ItemsPage, ItemDetails, DashboardPage, CalendarPage, ItemGrid, MiniCalendar.
 */
export function useItemStatus() {
  /**
   * Calculate days remaining until a given date
   * @param {string|Date} date - The expiration/renewal date
   * @returns {number|null} Number of days left (negative if expired), or null if no date
   */
  function daysLeft(date) {
    if (!date) return null
    return Math.ceil((new Date(date) - new Date()) / (1000 * 60 * 60 * 24))
  }

  /**
   * Get status object for an expiration date
   * @param {string|Date} date - The expiration/renewal date
   * @returns {Object} Status object with key, label, and color
   */
  function getStatus(date) {
    const diff = daysLeft(date)
    if (diff === null) return { key: "valid", label: "Valid", color: "green" }
    if (diff < 0)  return { key: "expired", label: "Expired",            color: "red"    }
    if (diff < 7)  return { key: "week",    label: "Expiring This Week", color: "yellow" }
    if (diff < 30) return { key: "soon",    label: "Expiring Soon",      color: "orange" }
    return { key: "valid", label: "Valid", color: "green" }
  }

  /**
   * Get Tailwind CSS classes for status badge
   * @param {string|Date} date - The expiration/renewal date
   * @returns {string} Tailwind CSS classes for the status badge
   */
  function getStatusColor(date) {
    const s = getStatus(date)
    const map = {
      expired: "bg-red-500/10 text-red-700 border-red-200",
      week:    "bg-yellow-500/10 text-yellow-700 border-yellow-200",
      soon:    "bg-orange-500/10 text-orange-700 border-orange-200",
      valid:   "bg-green-500/10 text-green-700 border-green-200",
    }
    return map[s.key]
  }

  return { daysLeft, getStatus, getStatusColor }
}
