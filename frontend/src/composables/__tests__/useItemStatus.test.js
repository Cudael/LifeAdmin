import { describe, it, expect, beforeEach, afterEach, vi } from 'vitest'
import { useItemStatus } from '../useItemStatus'

describe('useItemStatus', () => {
  const { daysLeft, getStatus, getStatusColor } = useItemStatus()

  const futureDate = (days) => {
    const d = new Date()
    d.setDate(d.getDate() + days)
    return d.toISOString()
  }

  it('returns null daysLeft for null date', () => {
    expect(daysLeft(null)).toBeNull()
  })

  it('calculates positive daysLeft for future date', () => {
    expect(daysLeft(futureDate(10))).toBeGreaterThan(0)
  })

  it('calculates negative daysLeft for past date', () => {
    expect(daysLeft(futureDate(-5))).toBeLessThan(0)
  })

  it('getStatus returns expired for past date', () => {
    expect(getStatus(futureDate(-1)).key).toBe('expired')
  })

  it('getStatus returns week for within 7 days', () => {
    expect(getStatus(futureDate(3)).key).toBe('week')
  })

  it('getStatus returns soon for within 30 days', () => {
    expect(getStatus(futureDate(15)).key).toBe('soon')
  })

  it('getStatus returns valid for far future', () => {
    expect(getStatus(futureDate(60)).key).toBe('valid')
  })

  it('getStatus returns valid for null date', () => {
    expect(getStatus(null).key).toBe('valid')
  })

  it('getStatusColor returns correct class for expired', () => {
    expect(getStatusColor(futureDate(-1))).toContain('red')
  })
})
