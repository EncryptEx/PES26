import { createI18n } from 'vue-i18n'

// Importem els diccionaris
import ca from './locales/ca.json'
import en from './locales/en.json'
import es from './locales/es.json'

// Busquem si l'usuari ja tenia un idioma guardat al navegador, sinó posem català per defecte
const savedLocale = localStorage.getItem('app-locale') || 'ca'

const i18n = createI18n({
  legacy: false,
  locale: savedLocale,
  fallbackLocale: 'en',
  messages: {
    ca,
    en,
    es
  }
})

export default i18n