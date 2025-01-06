<template>
  <div class="bg-gradient-to-br from-gray-50 to-gray-200 min-h-screen p-6">
    <div class="max-w-7xl mx-auto">
      
      <div class="bg-white shadow-2xl rounded-3xl overflow-hidden">
        <!-- Header -->
        <div class="bg-indigo-700 text-white p-6 shadow-lg">
          <div class="flex justify-between items-center">
            <div class="flex items-center space-x-4">
              <svg xmlns="http://www.w3.org/2000/svg" class="h-10 w-10" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                <line x1="12" y1="2" x2="12" y2="22"></line>
                <path d="M5 12l14 0"></path>
                <path d="M5 12l5 -5"></path>
                <path d="M5 12l5 5"></path>
                <path d="M19 12l-5 -5"></path>
                <path d="M19 12l-5 5"></path>
              </svg>
              <h1 class="text-4xl font-bold tracking-tight">Case à Choc - Tableau de Bord</h1>
            </div>
            <div class="flex space-x-4">
              <div class="relative">
                <button 
                  @click="toggleComparisonMode"
                  class="px-6 py-3 bg-white/20 text-white rounded-xl font-semibold hover:bg-white/30 transition-all flex items-center space-x-2"
                >
                  <svg xmlns="http://www.w3.org/2000/svg" class="h-5 w-5" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                    <path d="M3 3v18h18" />
                    <path d="M18 17l-6 -6l-6 6" />
                    <path d="M18 12l-6 -6l-6 6" />
                  </svg>
                  <span>{{ comparisonMode ? 'Quitter Comparaison' : 'Mode Comparaison' }}</span>
                </button>
              </div>
            </div>
          </div>
        </div>
<!-- Ajout de la section de KPIs juste après le header, avant les filtres -->
<div class="grid grid-cols-1 md:grid-cols-4 gap-6 p-6 bg-gray-50">
  <div class="bg-white shadow-md rounded-xl p-6 flex flex-col space-y-2">
    <div class="flex justify-between items-center">
      <span class="text-gray-500 text-sm uppercase">Ventes Totales</span>
      <svg xmlns="http://www.w3.org/2000/svg" class="h-6 w-6 text-indigo-600" fill="none" viewBox="0 0 24 24" stroke="currentColor">
        <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 8c-1.657 0-3 .895-3 2s1.343 2 3 2 3 .895 3 2-1.343 2-3 2m0-8c1.11 0 2.08.402 2.599 1M12 8V7m0 1v8m0 0v1m0-1c-1.11 0-2.08-.402-2.599-1M21 12a9 9 0 11-18 0 9 9 0 0118 0z" />
      </svg>
    </div>
    <div class="text-3xl font-bold text-gray-800">{{ totalSales }} CHF</div>
    <div class="flex items-center text-sm">
      <span :class="salesTrend >= 0 ? 'text-green-600' : 'text-red-600'">
        {{ salesTrend >= 0 ? '▲' : '▼' }} {{ Math.abs(salesTrend) }}%
      </span>
      <span class="ml-2 text-gray-500">vs période précédente</span>
    </div>
  </div>

  <div class="bg-white shadow-md rounded-xl p-6 flex flex-col space-y-2">
    <div class="flex justify-between items-center">
      <span class="text-gray-500 text-sm uppercase">Nombre de Billets</span>
      <svg xmlns="http://www.w3.org/2000/svg" class="h-6 w-6 text-green-600" fill="none" viewBox="0 0 24 24" stroke="currentColor">
        <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 12l2 2 4-4M7.835 4.697a3.42 3.42 0 001.946-.806 3.42 3.42 0 014.438 0 3.42 3.42 0 001.946.806 3.42 3.42 0 013.138 3.138 3.42 3.42 0 00.806 1.946 3.42 3.42 0 010 4.438 3.42 3.42 0 00-.806 1.946 3.42 3.42 0 01-3.138 3.138 3.42 3.42 0 00-1.946.806 3.42 3.42 0 01-4.438 0 3.42 3.42 0 00-1.946-.806 3.42 3.42 0 01-3.138-3.138 3.42 3.42 0 00-.806-1.946 3.42 3.42 0 010-4.438 3.42 3.42 0 00.806-1.946 3.42 3.42 0 013.138-3.138z" />
      </svg>
    </div>
    <div class="text-3xl font-bold text-gray-800">{{ totalTickets }}</div>
    <div class="flex items-center text-sm">
      <span :class="ticketsTrend >= 0 ? 'text-green-600' : 'text-red-600'">
        {{ ticketsTrend >= 0 ? '▲' : '▼' }} {{ Math.abs(ticketsTrend) }}%
      </span>
      <span class="ml-2 text-gray-500">vs période précédente</span>
    </div>
  </div>

  <div class="bg-white shadow-md rounded-xl p-6 flex flex-col space-y-2">
    <div class="flex justify-between items-center">
      <span class="text-gray-500 text-sm uppercase">Événements Uniques</span>
      <svg xmlns="http://www.w3.org/2000/svg" class="h-6 w-6 text-blue-600" fill="none" viewBox="0 0 24 24" stroke="currentColor">
        <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 12l2 2 4-4M7.835 4.697a3.42 3.42 0 001.946-.806 3.42 3.42 0 014.438 0 3.42 3.42 0 001.946.806 3.42 3.42 0 013.138 3.138 3.42 3.42 0 00.806 1.946 3.42 3.42 0 010 4.438 3.42 3.42 0 00-.806 1.946 3.42 3.42 0 01-3.138 3.138 3.42 3.42 0 00-1.946.806 3.42 3.42 0 01-4.438 0 3.42 3.42 0 00-1.946-.806 3.42 3.42 0 01-3.138-3.138 3.42 3.42 0 00-.806-1.946 3.42 3.42 0 010-4.438 3.42 3.42 0 00.806-1.946 3.42 3.42 0 013.138-3.138z" />
      </svg>
    </div>
    <div class="text-3xl font-bold text-gray-800">{{ uniqueEventsCount }}</div>
    <div class="flex items-center text-sm">
      <span :class="uniqueEventsTrend >= 0 ? 'text-green-600' : 'text-red-600'">
        {{ uniqueEventsTrend >= 0 ? '▲' : '▼' }} {{ Math.abs(uniqueEventsTrend) }}%
      </span>
      <span class="ml-2 text-gray-500">vs période précédente</span>
    </div>
  </div>

  <div class="bg-white shadow-md rounded-xl p-6 flex flex-col space-y-2">
    <div class="flex justify-between items-center">
      <span class="text-gray-500 text-sm uppercase">Taux de Remplissage</span>
      <svg xmlns="http://www.w3.org/2000/svg" class="h-6 w-6 text-purple-600" fill="none" viewBox="0 0 24 24" stroke="currentColor">
        <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 12l2 2 4-4m6 2a9 9 0 11-18 0 9 9 0 0118 0z" />
      </svg>
    </div>
    <div class="text-3xl font-bold text-gray-800">{{ occupancyRate }}%</div>
    <div class="flex items-center text-sm">
      <span :class="occupancyTrend >= 0 ? 'text-green-600' : 'text-red-600'">
        {{ occupancyTrend >= 0 ? '▲' : '▼' }} {{ Math.abs(occupancyTrend) }}%
      </span>
      <span class="ml-2 text-gray-500">vs période précédente</span>
    </div>
  </div>
</div>
        <!-- Filtres et Sélection -->
        <div class="p-6 bg-gray-50 border-b">
          <div class="grid grid-cols-1 md:grid-cols-3 gap-6">
            <div>
              <label class="block text-sm font-medium text-gray-700 mb-2">Événements</label>
              <select 
                v-model="selectedEvents" 
                multiple 
                class="w-full border-gray-300 rounded-xl shadow-sm focus:ring-indigo-500 focus:border-indigo-500"
              >
                <option 
                  v-for="event in uniqueEvents" 
                  :key="event" 
                  :value="event"
                >
                  {{ event }}
                </option>
              </select>
            </div>
            
            <div v-if="comparisonMode">
              <label class="block text-sm font-medium text-gray-700 mb-2">Dimension de Comparaison</label>
              <select 
                v-model="comparisonDimension" 
                class="w-full border-gray-300 rounded-xl shadow-sm focus:ring-indigo-500 focus:border-indigo-500"
              >
                <option value="promoter">Promoteur</option>
                <option value="category">Catégorie</option>
                <option value="price">Fourchette de Prix</option>
              </select>
            </div>

            <div>
              <label class="block text-sm font-medium text-gray-700 mb-2">Période</label>
              <div class="flex space-x-2">
                <input 
                  type="date" 
                  v-model="startDate"
                  class="w-full border-gray-300 rounded-xl shadow-sm focus:ring-indigo-500 focus:border-indigo-500"
                >
                <input 
                  type="date" 
                  v-model="endDate"
                  class="w-full border-gray-300 rounded-xl shadow-sm focus:ring-indigo-500 focus:border-indigo-500"
                >
              </div>
            </div>
          </div>
        </div>

        <!-- Graphiques Principaux -->
        <div class="grid grid-cols-1 lg:grid-cols-2 gap-8 p-8">
          <!-- Graphique des Ventes par Jour -->
          <div class="bg-white border rounded-2xl p-6 shadow-lg">
            <div class="flex justify-between items-center mb-6">
              <h2 class="text-2xl font-semibold text-gray-800">Ventes Journalières</h2>
              <div class="flex space-x-2">
    <button 
      @click="selectedTimeScale = 'daily'"
      :class="['px-3 py-1 rounded', selectedTimeScale === 'daily' ? 'bg-indigo-100 text-indigo-700' : 'text-gray-600 hover:bg-gray-100']"
    >
      Journalier
    </button>
    <button 
      @click="selectedTimeScale = 'weekly'"
      :class="['px-3 py-1 rounded', selectedTimeScale === 'weekly' ? 'bg-indigo-100 text-indigo-700' : 'text-gray-600 hover:bg-gray-100']"
    >
      Hebdomadaire
    </button>
    <div class="flex items-center space-x-2">
      <button 
        @click="selectedTimeScale = 'days-before'"
        :class="['px-3 py-1 rounded', selectedTimeScale === 'days-before' ? 'bg-indigo-100 text-indigo-700' : 'text-gray-600 hover:bg-gray-100']"
      >
        J-
      </button>
      <input 
        type="number" 
        v-model.number="daysBeforeEventInput" 
        placeholder="Jours avant"
        class="w-20 border-gray-300 rounded-xl shadow-sm focus:ring-indigo-500 focus:border-indigo-500"
        v-if="selectedTimeScale === 'days-before'"
      >
    </div>
  </div>
            </div>
            <Line 
              v-if="tickets.length"
              :data="lineChartData" 
              :options="lineChartOptions"
              class="h-96"
            />
            <p v-else class="text-center text-gray-500">Aucune donnée disponible</p>
          </div>

          <!-- Graphique de Répartition des Événements -->
          <div class="bg-white border rounded-2xl p-6 shadow-lg">
            <h2 class="text-2xl font-semibold mb-6 text-gray-800">Répartition des Événements</h2>
            <Pie 
              v-if="tickets.length"
              :data="pieChartData" 
              :options="pieChartOptions"
              class="h-96"
            />
            <p v-else class="text-center text-gray-500">Aucune donnée disponible</p>
          </div>
        </div>
        <div class="bg-white border rounded-2xl p-6 shadow-lg">
    <h2 class="text-2xl font-semibold mb-6 text-gray-800">Origine Géographique des Acheteurs</h2>
    <Pie 
      v-if="filteredTickets.length"
      :data="buyerLocationData" 
      :options="pieChartOptions"
      class="h-12"
    />
    <p v-else class="text-center text-gray-500">Aucune donnée disponible</p>
  </div>
        <!-- Tableau de Comparaison -->
        <div v-if="comparisonMode" class="p-8">
          <h2 class="text-3xl font-bold mb-6 text-gray-900">Analyse Comparative</h2>
          <div class="bg-white border rounded-2xl overflow-hidden shadow-xl">
            <table class="w-full">
              <thead class="bg-gray-100">
                <tr>
                  <th class="px-6 py-4 text-left text-xs font-medium text-gray-500 uppercase tracking-wider">
                    {{ comparisonDimension }}
                  </th>
                  <th 
                    v-for="event in selectedEvents" 
                    :key="event" 
                    class="px-6 py-4 text-left text-xs font-medium text-gray-500 uppercase tracking-wider"
                  >
                    {{ event }}
                  </th>
                </tr>
              </thead>
              <tbody>
                <tr 
                  v-for="(row, index) in comparisonTableData" 
                  :key="index" 
                  class="border-b hover:bg-gray-50 transition"
                >
                  <td class="px-6 py-4 whitespace-nowrap font-medium text-gray-900">
                    {{ row.label }}
                  </td>
                  <td 
                    v-for="event in selectedEvents" 
                    :key="event" 
                    class="px-6 py-4 whitespace-nowrap"
                  >
                    {{ row.data[event] || 'N/A' }}
                  </td>
                </tr>
              </tbody>
            </table>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref, computed, onMounted, watch } from 'vue'
import { collection, getDocs, query, where } from 'firebase/firestore'
import { Line, Pie } from 'vue-chartjs'
import { db } from '../firebase'
import {
  Chart,
  Title,
  Tooltip,
  Legend,
  LineElement,
  CategoryScale,
  LinearScale,
  PointElement,
  ArcElement
} from 'chart.js'

Chart.register(
  Title,
  Tooltip,
  Legend,
  LineElement,
  CategoryScale,
  LinearScale,
  PointElement,
  ArcElement
)
const daysBeforeEventInput = ref(0)

const totalSales = computed(() => {
  // Ajout de vérifications pour gérer différents formats potentiels de prix
  return filteredTickets.value.reduce((total, ticket) => {
    const price = ticket.price?.amount || ticket.price || 0
    return total + (typeof price === 'number' ? price : parseFloat(price))
  }, 0).toFixed(2)
})

const totalTickets = computed(() => {
  return filteredTickets.value.length
})

const uniqueEventsCount = computed(() => {
  return new Set(filteredTickets.value.map(ticket => ticket.event)).size
})

const occupancyRate = computed(() => {
  // Calcul simplifié du taux de remplissage
  const maxCapacity = filteredTickets.value.reduce((acc, ticket) => {
    acc[ticket.event] = (acc[ticket.event] || 0) + 1
    return acc
  }, {})

  const occupancyPerEvent = Object.entries(maxCapacity).map(([event, count]) => 
    Math.min((count / 100) * 100, 100)
  )

  return occupancyPerEvent.length > 0 
    ? (occupancyPerEvent.reduce((a, b) => a + b, 0) / occupancyPerEvent.length).toFixed(1)
    : 0
})

const tickets = ref([])
const selectedEvents = ref([])
const comparisonMode = ref(false)
const comparisonDimension = ref('promoter')
const selectedTimeScale = ref('daily')
const daysBeforeEvent = ref(0)
const startDate = ref('')
const endDate = ref('')

const calculateTrend = (currentPeriod, previousPeriod) => {
  if (previousPeriod === 0) return 0
  return ((currentPeriod - previousPeriod) / previousPeriod * 100).toFixed(1)
}

const salesTrend = computed(() => {
  const currentPeriodSales = filteredTickets.value.reduce((total, ticket) => {
    const price = ticket.price?.amount || ticket.price || 0
    return total + (typeof price === 'number' ? price : parseFloat(price))
  }, 0)
  
  // Filtrer les tickets de la période précédente
  const previousPeriodTickets = tickets.value.filter(ticket => {
    const ticketDate = new Date(ticket.generatedAt)
    const currentStartDate = startDate.value ? new Date(startDate.value) : null
    const currentEndDate = endDate.value ? new Date(endDate.value) : null
    
    // Si des dates sont sélectionnées, calculer la période précédente
    if (currentStartDate && currentEndDate) {
      const periodDuration = (currentEndDate - currentStartDate) / (24 * 60 * 60 * 1000)
      const previousStartDate = new Date(currentStartDate)
      previousStartDate.setDate(previousStartDate.getDate() - periodDuration)
      const previousEndDate = new Date(currentStartDate)
      
      return ticketDate >= previousStartDate && ticketDate < currentStartDate
    }
    
    // Si aucune date n'est sélectionnée, prendre une période par défaut (par exemple, le mois précédent)
    const currentDate = new Date()
    const previousMonthStart = new Date(currentDate.getFullYear(), currentDate.getMonth() - 1, 1)
    const previousMonthEnd = new Date(currentDate.getFullYear(), currentDate.getMonth(), 0)
    
    return ticketDate >= previousMonthStart && ticketDate <= previousMonthEnd
  })
  
  const previousPeriodSales = previousPeriodTickets.reduce((total, ticket) => {
    const price = ticket.price?.amount || ticket.price || 0
    return total + (typeof price === 'number' ? price : parseFloat(price))
  }, 0)
  
  return calculateTrend(currentPeriodSales, previousPeriodSales)
})

const ticketsTrend = computed(() => {
  const currentPeriodTickets = filteredTickets.value.length
  
  const previousPeriodTickets = tickets.value.filter(ticket => {
    const ticketDate = new Date(ticket.generatedAt)
    const currentStartDate = startDate.value ? new Date(startDate.value) : null
    const currentEndDate = endDate.value ? new Date(endDate.value) : null
    
    // Logique similaire à salesTrend pour définir la période précédente
    if (currentStartDate && currentEndDate) {
      const periodDuration = (currentEndDate - currentStartDate) / (24 * 60 * 60 * 1000)
      const previousStartDate = new Date(currentStartDate)
      previousStartDate.setDate(previousStartDate.getDate() - periodDuration)
      const previousEndDate = new Date(currentStartDate)
      
      return ticketDate >= previousStartDate && ticketDate < currentStartDate
    }
    
    const currentDate = new Date()
    const previousMonthStart = new Date(currentDate.getFullYear(), currentDate.getMonth() - 1, 1)
    const previousMonthEnd = new Date(currentDate.getFullYear(), currentDate.getMonth(), 0)
    
    return ticketDate >= previousMonthStart && ticketDate <= previousMonthEnd
  }).length
  
  return calculateTrend(currentPeriodTickets, previousPeriodTickets)
})

const uniqueEventsTrend = computed(() => {
  const currentUniqueEvents = new Set(filteredTickets.value.map(ticket => ticket.event)).size
  
  const previousPeriodTickets = tickets.value.filter(ticket => {
    const ticketDate = new Date(ticket.generatedAt)
    const currentStartDate = startDate.value ? new Date(startDate.value) : null
    const currentEndDate = endDate.value ? new Date(endDate.value) : null
    
    // Logique similaire aux précédentes pour définir la période précédente
    if (currentStartDate && currentEndDate) {
      const periodDuration = (currentEndDate - currentStartDate) / (24 * 60 * 60 * 1000)
      const previousStartDate = new Date(currentStartDate)
      previousStartDate.setDate(previousStartDate.getDate() - periodDuration)
      const previousEndDate = new Date(currentStartDate)
      
      return ticketDate >= previousStartDate && ticketDate < currentStartDate
    }
    
    const currentDate = new Date()
    const previousMonthStart = new Date(currentDate.getFullYear(), currentDate.getMonth() - 1, 1)
    const previousMonthEnd = new Date(currentDate.getFullYear(), currentDate.getMonth(), 0)
    
    return ticketDate >= previousMonthStart && ticketDate <= previousMonthEnd
  })
  
  const previousUniqueEvents = new Set(previousPeriodTickets.map(ticket => ticket.event)).size
  
  return calculateTrend(currentUniqueEvents, previousUniqueEvents)
})

const occupancyTrend = computed(() => {
  const calculateOccupancyRate = (tickets) => {
    const maxCapacity = tickets.reduce((acc, ticket) => {
      acc[ticket.event] = (acc[ticket.event] || 0) + 1
      return acc
    }, {})

    const occupancyPerEvent = Object.entries(maxCapacity).map(([event, count]) => 
      Math.min((count / 100) * 100, 100)
    )

    return occupancyPerEvent.length > 0 
      ? (occupancyPerEvent.reduce((a, b) => a + b, 0) / occupancyPerEvent.length)
      : 0
  }

  const currentOccupancyRate = calculateOccupancyRate(filteredTickets.value)
  
  const previousPeriodTickets = tickets.value.filter(ticket => {
    const ticketDate = new Date(ticket.generatedAt)
    const currentStartDate = startDate.value ? new Date(startDate.value) : null
    const currentEndDate = endDate.value ? new Date(endDate.value) : null
    
    // Logique similaire aux précédentes pour définir la période précédente
    if (currentStartDate && currentEndDate) {
      const periodDuration = (currentEndDate - currentStartDate) / (24 * 60 * 60 * 1000)
      const previousStartDate = new Date(currentStartDate)
      previousStartDate.setDate(previousStartDate.getDate() - periodDuration)
      const previousEndDate = new Date(currentStartDate)
      
      return ticketDate >= previousStartDate && ticketDate < currentStartDate
    }
    
    const currentDate = new Date()
    const previousMonthStart = new Date(currentDate.getFullYear(), currentDate.getMonth() - 1, 1)
    const previousMonthEnd = new Date(currentDate.getFullYear(), currentDate.getMonth(), 0)
    
    return ticketDate >= previousMonthStart && ticketDate <= previousMonthEnd
  })
  
  const previousOccupancyRate = calculateOccupancyRate(previousPeriodTickets)
  
  return calculateTrend(currentOccupancyRate, previousOccupancyRate)
})

const uniqueEvents = computed(() => {
  return [...new Set(tickets.value.map(ticket => ticket.event))]
})

const filteredTickets = computed(() => {
  return tickets.value.filter(ticket => {
    const eventMatch = selectedEvents.value.length === 0 || 
      selectedEvents.value.includes(ticket.event)
    
    const dateMatch = (!startDate.value || new Date(ticket.generatedAt) >= new Date(startDate.value)) &&
      (!endDate.value || new Date(ticket.generatedAt) <= new Date(endDate.value))
    
    return eventMatch && dateMatch
  })
})


const lineChartData = computed(() => {
  const salesData = {}
  
  let dateGroups
  switch(selectedTimeScale.value) {
    case 'daily':
      dateGroups = [...new Set(filteredTickets.value.map(ticket => safeParseDate(ticket.generatedAt).toISOString().split('T')[0]))]
      break
    case 'weekly':
      dateGroups = groupDatesByWeek(filteredTickets.value.map(ticket => ticket.generatedAt))
      break
    case 'days-before':
      dateGroups = generateDaysBeforeEventLabels(filteredTickets.value, daysBeforeEventInput.value)
      break
  }

  dateGroups.forEach(dateGroup => {
    salesData[dateGroup] = salesData[dateGroup] || {}
    filteredTickets.value
      .filter(ticket => {
        const ticketDate = safeParseDate(ticket.generatedAt).toISOString().split('T')[0]
        switch(selectedTimeScale.value) {
          case 'daily':
            return ticketDate === dateGroup
          case 'weekly':
            return weekOfDate(ticket.generatedAt) === dateGroup
          case 'days-before':
          const daysBeforeInput = daysBeforeEventInput.value || 0
  dateGroups = generateDaysBeforeEventLabels(filteredTickets.value, daysBeforeInput)
  break
        }
      })
      .forEach(ticket => {
        salesData[dateGroup][ticket.event] = 
          (salesData[dateGroup][ticket.event] || 0) + 1
      })
  })

  const sortedDates = Object.keys(salesData).sort()

  return {
    labels: selectedTimeScale.value === 'days-before'
      ? sortedDates.map(date => {
          const eventDate = safeParseDate(filteredTickets.value.find(t => t.eventDate)?.eventDate)
          return `J-${Math.abs(Math.round((eventDate - safeParseDate(date)) / (1000 * 60 * 60 * 24)))}`
        })
      : sortedDates,
    datasets: selectedEvents.value.length > 0 
      ? selectedEvents.value.map((event, index) => ({
          label: event,
          data: sortedDates.map(date => salesData[date][event] || 0),
          borderColor: getColor(index),
          backgroundColor: getColor(index, 0.2),
          tension: 0.4,
          fill: true
        }))
      : [{
          label: 'Tous les événements',
          data: sortedDates.map(date => 
            Object.values(salesData[date] || {}).reduce((a, b) => a + b, 0)
          ),
          borderColor: getColor(0),
          backgroundColor: getColor(0, 0.2),
          tension: 0.4,
          fill: true
        }]
  }
})

function safeParseDate(dateStr) {
  const parsed = new Date(dateStr)
  return isNaN(parsed) ? new Date() : parsed
}
function generateDaysBeforeEventLabels(tickets, daysBeforeEvent) {
  const allDates = []
  const eventDates = [...new Set(tickets.map(ticket => ticket.sessions[0].date))]
  
  eventDates.forEach(eventDateStr => {
    const eventDate = safeParseDate(eventDateStr)
    const labels = []
    
    // Générer des labels pour daysBeforeEvent jours avant l'événement
    for (let i = daysBeforeEvent; i > 0; i--) {
      const date = new Date(eventDate)
      date.setDate(eventDate.getDate() - i)
      labels.push(date.toISOString().split('T')[0])
    }
    
    allDates.push(...labels)
  })
  
  return [...new Set(allDates)].sort()
}
const pieChartData = computed(() => {
  const eventCounts = {}
  
  filteredTickets.value.forEach(ticket => {
    eventCounts[ticket.event] = (eventCounts[ticket.event] || 0) + 1
  })

  return {
    labels: Object.keys(eventCounts),
    datasets: [{
      data: Object.values(eventCounts),
      backgroundColor: Object.keys(eventCounts).map((_, index) => getColor(index, 0.6))
    }]
  }
})

const comparisonTableData = computed(() => {
  if (!comparisonMode.value) return []

  const dimensionData = {}
  
  filteredTickets.value.forEach(ticket => {
    let key
    switch(comparisonDimension.value) {
      case 'promoter':
        key = ticket.promoter
        break
      case 'category':
        key = ticket.category
        break
      case 'price':
        key = getPriceRange(ticket.price.amount)
        break
    }

    if (!dimensionData[key]) {
      dimensionData[key] = {}
    }
    dimensionData[key][ticket.event] = (dimensionData[key][ticket.event] || 0) + 1
  })

  return Object.entries(dimensionData).map(([label, data]) => ({
    label,
    data
  }))
})

const lineChartOptions = {
  responsive: true,
  scales: {
    y: {
      beginAtZero: true,
      title: {
        display: true,
        text: 'Nombre de billets'
      }
    }
  },
  plugins: {
    legend: {
      position: 'bottom'
    }
  }
}

const pieChartOptions = {
  responsive: true,
  plugins: {
    legend: {
      position: 'bottom'
    }
  }
}
const POSTCODE_TO_CITY = {
  '1000': 'Lausanne',
  '1004': 'Lausanne',
  '1005': 'Lausanne',
  '1006': 'Lausanne',
  '1007': 'Lausanne',
  '1008': 'Lausanne',
  '1009': 'Lausanne',
  '1010': 'Lausanne',
  '1011': 'Lausanne',
  '1012': 'Lausanne',
  '1018': 'Lausanne',
  
  '1003': 'Lausanne-Sébeillon',
  '1002': 'Lausanne-Flon',
  
  '1110': 'Morges',
  '1131': 'Tolochenaz',
  '1124': 'Gollion',
  
  '1009': 'Pully',
  '1090': 'La Croix-sur-Lutry',
  
  '1260': 'Nyon',
  '1262': 'Eysins',
  
  '1004': 'Chauderon',
  
  '1007': 'Rumine',
  '1005': 'Bourdonette',
  
  '1010': 'Secteur Riponne',
  '1011': 'Secteur Montbenon',
  
  '2000': 'Neuchâtel',
  '2002': 'Neuchâtel',
  
  '1200': 'Genève',
  '1202': 'Genève',
  '1203': 'Genève',
  '1204': 'Genève',
  '1205': 'Genève',
  '1206': 'Genève',
  '1207': 'Genève',
  '1208': 'Genève',
  
  '1800': 'Vevey',
  '1820': 'Montreux',
  
  // Ajoutez plus de codes postaux selon vos besoins
  
  // Ville par défaut si le code postal n'est pas reconnu
  'default': 'Autre ville'
}

const buyerLocationData = computed(() => {
  const cityCounts = {}
  
  filteredTickets.value.forEach(ticket => {
    const postcode = ticket.buyer?.postcode || ''
    // Convertir le code postal en nom de ville, avec une ville par défaut
    const city = POSTCODE_TO_CITY[postcode] || POSTCODE_TO_CITY['default']
    
    cityCounts[city] = (cityCounts[city] || 0) + 1
  })

  // Trier les villes par nombre de billets (décroissant)
  const sortedCities = Object.entries(cityCounts)
    .sort((a, b) => b[1] - a[1])
    .reduce((acc, [city, count]) => {
      acc[city] = count
      return acc
    }, {})

  return {
    labels: Object.keys(sortedCities),
    datasets: [{
      data: Object.values(sortedCities),
      backgroundColor: Object.keys(sortedCities).map((_, index) => getColor(index, 0.6))
    }]
  }
})
function getColor(index, opacity = 1) {
  const colors = [
    `rgba(54, 162, 235, ${opacity})`,
    `rgba(255, 99, 132, ${opacity})`,
    `rgba(75, 192, 192, ${opacity})`,
    `rgba(255, 206, 86, ${opacity})`,
    `rgba(153, 102, 255, ${opacity})`
  ]
  return colors[index % colors.length]
}

function getPriceRange(price) {
  if (price < 50) return '< 50 CHF'
  if (price < 100) return '50 - 100 CHF'
  if (price < 200) return '100 - 200 CHF'
  return '> 200 CHF'
}

function weekOfDate(dateStr) {
  const d = safeParseDate(dateStr)
  const firstDayOfWeek = new Date(d)
  firstDayOfWeek.setDate(d.getDate() - d.getDay() + (d.getDay() === 0 ? -6 : 1))
  return firstDayOfWeek.toISOString().split('T')[0]
}

function groupDatesByWeek(dates) {
  return [...new Set(dates.map(dateStr => {
    const d = safeParseDate(dateStr)
    const firstDayOfWeek = new Date(d)
    firstDayOfWeek.setDate(d.getDate() - d.getDay() + (d.getDay() === 0 ? -6 : 1))
    return firstDayOfWeek.toISOString().split('T')[0]
  }))]
}

async function fetchTickets() {
  const q = query(collection(db, 'tickets'))
  const querySnapshot = await getDocs(q)
  tickets.value = querySnapshot.docs.map(doc => doc.data())
}

function toggleComparisonMode() {
  comparisonMode.value = !comparisonMode.value
}

onMounted(fetchTickets)
watch([selectedEvents, startDate, endDate], fetchTickets)

</script>