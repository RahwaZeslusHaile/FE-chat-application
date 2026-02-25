/**
 * Date and Time utilities for handling timezone conversions
 * Follows Single Responsibility Principle (SRP)
 */

/**
 * Converts browser local datetime to UTC ISO string
 * 
 * @param {string} localDateTimeString - HTML datetime-local input value (e.g., "2026-02-25T15:00")
 * @returns {string|null} UTC ISO 8601 string (e.g., "2026-02-25T20:00:00.000Z") or null if input is falsy
 * 
 * @example
 * convertToUTC("2026-02-25T15:00") // EST → "2026-02-25T20:00:00.000Z"
 */
export const convertToUTC = (localDateTimeString) => {
  if (!localDateTimeString) return null;

  const localDate = new Date(localDateTimeString);

  const utcDate = new Date(
    localDate.getTime() - localDate.getTimezoneOffset() * 60000
  );

  return utcDate.toISOString();
};

/**
 * Formats datetime for display purposes (e.g., "Feb 25, 3:00 PM")
 * 
 * @param {string} isoDateString - ISO 8601 datetime string
 * @returns {string} Formatted datetime string
 * 
 * @example
 * formatDateTime("2026-02-25T20:00:00.000Z") // "Feb 25, 8:00 PM"
 */
export const formatDateTime = (isoDateString) => {
  if (!isoDateString) return "";

  const date = new Date(isoDateString);
  return date.toLocaleString("en-US", {
    month: "short",
    day: "numeric",
    hour: "numeric",
    minute: "2-digit",
    hour12: true,
  });
};

/**
 * Checks if a scheduled datetime is in the past
 * 
 * @param {string} isoDateString - ISO 8601 datetime string
 * @returns {boolean} True if the datetime is in the past
 * 
 * @example
 * isInPast("2026-02-25T15:00:00.000Z") // false (future)
 * isInPast("2024-02-25T15:00:00.000Z") // true (past)
 */
export const isInPast = (isoDateString) => {
  if (!isoDateString) return false;

  const scheduledTime = new Date(isoDateString).getTime();
  const now = new Date().getTime();

  return scheduledTime < now;
};

/**
 * Gets minimum datetime for input (current time)
 * Used to prevent scheduling messages in the past
 * 
 * @returns {string} Current datetime in datetime-local format
 * 
 * @example
 * getMinDateTime() // "2026-02-25T14:30"
 */
export const getMinDateTime = () => {
  const now = new Date();
  now.setMinutes(now.getMinutes() - now.getTimezoneOffset());
  return now.toISOString().slice(0, 16);
};
