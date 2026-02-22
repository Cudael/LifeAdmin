const BASE = "/src/assets/item-type-images/"

export const DEFAULT_IMAGE = `${BASE}default.jpg`

export const itemTypeImages = {
  // Documents
  "passport": `${BASE}passport.jpg`,
  "visa": `${BASE}visa.jpg`,
  "drivers-license": `${BASE}drivers-license.jpg`,
  "id-card": `${BASE}id-card.jpg`,
  "health-insurance-card": `${BASE}health-insurance-card.jpg`,
  "warranty": `${BASE}warranty.jpg`,
  "credit-card": `${BASE}credit-card.jpg`,
  "bank-account": `${BASE}bank-account.jpg`,
  "tax-document": `${BASE}tax-document.jpg`,
  "professional-certificate": `${BASE}professional-certificate.jpg`,
  "professional-license": `${BASE}professional-license.jpg`,
  "lease-agreement": `${BASE}lease-agreement.jpg`,
  "property-deed": `${BASE}property-deed.jpg`,
  "legal-contract": `${BASE}legal-contract.jpg`,
  "vehicle-registration": `${BASE}vehicle-registration.jpg`,
  "generic-document": `${BASE}generic-document.jpg`,

  // Existing subscriptions
  "netflix": `${BASE}netflix.jpg`,
  "spotify": `${BASE}spotify.jpg`,
  "gym-membership": `${BASE}gym-membership.jpg`,
  "github": `${BASE}github.jpg`,
  "dropbox": `${BASE}dropbox.jpg`,
  "adobe-creative-cloud": `${BASE}adobe-creative-cloud.jpg`,
  "microsoft-365": `${BASE}microsoft-365.jpg`,
  "auto-insurance": `${BASE}auto-insurance.jpg`,
  "professional-membership": `${BASE}professional-membership.jpg`,
  "generic-subscription": `${BASE}generic-subscription.jpg`,

  // New streaming / video subscriptions
  "youtube-premium": `${BASE}youtube-premium.jpg`,
  "disney-plus": `${BASE}disney-plus.jpg`,
  "hbo-max": `${BASE}hbo-max.jpg`,
  "amazon-prime": `${BASE}amazon-prime.jpg`,
  "apple-tv-plus": `${BASE}apple-tv-plus.jpg`,
  "hulu": `${BASE}hulu.jpg`,
  "paramount-plus": `${BASE}paramount-plus.jpg`,
  "crunchyroll": `${BASE}crunchyroll.jpg`,
  "twitch": `${BASE}twitch.jpg`,

  // New music subscriptions
  "apple-music": `${BASE}apple-music.jpg`,
  "tidal": `${BASE}tidal.jpg`,
  "youtube-music": `${BASE}youtube-music.jpg`,

  // New cloud / productivity subscriptions
  "google-one": `${BASE}google-one.jpg`,
  "icloud-plus": `${BASE}icloud-plus.jpg`,
  "notion": `${BASE}notion.jpg`,
  "slack": `${BASE}slack.jpg`,
  "zoom": `${BASE}zoom.jpg`,

  // New gaming subscriptions
  "playstation-plus": `${BASE}playstation-plus.jpg`,
  "xbox-game-pass": `${BASE}xbox-game-pass.jpg`,
  "nintendo-switch-online": `${BASE}nintendo-switch-online.jpg`,
  "steam": `${BASE}steam.jpg`,

  // New other popular subscriptions
  "chatgpt-plus": `${BASE}chatgpt-plus.jpg`,
  "nordvpn": `${BASE}nordvpn.jpg`,
  "expressvpn": `${BASE}expressvpn.jpg`,
  "duolingo": `${BASE}duolingo.jpg`,
  "audible": `${BASE}audible.jpg`,
  "kindle-unlimited": `${BASE}kindle-unlimited.jpg`,
}

// Keyword map: maps search keywords to image keys in itemTypeImages
const keywordMap = [
  ["passport", "passport"],
  ["visa", "visa"],
  ["driver", "drivers-license"],
  ["license", "drivers-license"],
  ["id card", "id-card"],
  ["health insurance", "health-insurance-card"],
  ["warranty", "warranty"],
  ["credit card", "credit-card"],
  ["bank account", "bank-account"],
  ["tax", "tax-document"],
  ["professional certificate", "professional-certificate"],
  ["certificate", "professional-certificate"],
  ["professional license", "professional-license"],
  ["lease", "lease-agreement"],
  ["property deed", "property-deed"],
  ["deed", "property-deed"],
  ["legal contract", "legal-contract"],
  ["contract", "legal-contract"],
  ["vehicle registration", "vehicle-registration"],
  ["registration", "vehicle-registration"],
  ["netflix", "netflix"],
  ["spotify", "spotify"],
  ["gym", "gym-membership"],
  ["github", "github"],
  ["dropbox", "dropbox"],
  ["adobe", "adobe-creative-cloud"],
  ["creative cloud", "adobe-creative-cloud"],
  ["microsoft 365", "microsoft-365"],
  ["microsoft365", "microsoft-365"],
  ["office 365", "microsoft-365"],
  ["auto insurance", "auto-insurance"],
  ["car insurance", "auto-insurance"],
  ["professional membership", "professional-membership"],
  ["youtube premium", "youtube-premium"],
  ["disney", "disney-plus"],
  ["hbo", "hbo-max"],
  ["amazon prime", "amazon-prime"],
  ["prime video", "amazon-prime"],
  ["apple tv", "apple-tv-plus"],
  ["hulu", "hulu"],
  ["paramount", "paramount-plus"],
  ["crunchyroll", "crunchyroll"],
  ["twitch", "twitch"],
  ["apple music", "apple-music"],
  ["tidal", "tidal"],
  ["youtube music", "youtube-music"],
  ["google one", "google-one"],
  ["icloud", "icloud-plus"],
  ["notion", "notion"],
  ["slack", "slack"],
  ["zoom", "zoom"],
  ["playstation", "playstation-plus"],
  ["ps plus", "playstation-plus"],
  ["xbox", "xbox-game-pass"],
  ["game pass", "xbox-game-pass"],
  ["nintendo", "nintendo-switch-online"],
  ["steam", "steam"],
  ["chatgpt", "chatgpt-plus"],
  ["nordvpn", "nordvpn"],
  ["expressvpn", "expressvpn"],
  ["duolingo", "duolingo"],
  ["audible", "audible"],
  ["kindle", "kindle-unlimited"],
]

/**
 * Returns the image path for the given item type name.
 * Performs case-insensitive keyword matching.
 * Falls back to DEFAULT_IMAGE if no match is found.
 *
 * @param {string} itemTypeName
 * @returns {string} image path
 */
export function getItemTypeImage(itemTypeName) {
  if (!itemTypeName) return DEFAULT_IMAGE

  const lower = itemTypeName.toLowerCase()

  for (const [keyword, key] of keywordMap) {
    if (lower.includes(keyword)) {
      return itemTypeImages[key] || DEFAULT_IMAGE
    }
  }

  return DEFAULT_IMAGE
}
