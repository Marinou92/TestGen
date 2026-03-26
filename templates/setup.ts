import '@testing-library/jest-dom/vitest'
import { afterEach, vi } from 'vitest'
import { cleanup } from '@testing-library/react'

afterEach(() => {
  cleanup()
  vi.clearAllMocks()
  vi.restoreAllMocks()
})

if (!globalThis.fetch) {
  globalThis.fetch = vi.fn() as typeof fetch
}

if (!process.env.NODE_ENV) {
  process.env.NODE_ENV = 'test'
}
