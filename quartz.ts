import { loadQuartzConfig, loadQuartzLayout } from "./quartz/plugins/loader/config-loader"
import * as ExternalPlugin from "./.quartz/plugins"
import type { ExplorerOptions } from "./.quartz/plugins"

/* Explorer customize */
// add explorer customizations, cf. https://quartz.jzhao.xyz/features/explorer
export const explMapFn : ExplorerOptions["mapFn"] =
(node) => {
  if (node.isFolder) {
    node.displayName = "📁 " + node.displayName
  } else {
    node.displayName = "📄 " + node.displayName
  }
  return node
}

export const explFilterFn : ExplorerOptions["filterFn"] =
(node) => {
  // set containing names of everything you want to filter out
    const omit = new Set(["assets", "tags", "advanced"])
 
    // can also use node.slug or by anything on node.data
    // note that node.data is only present for files that exist on disk
    // (e.g. implicit folder nodes that have no associated index.md)
    const name = node.displayName?.toLowerCase()
    console.log("name:", name, "-- slug:", node.slugSegment)
    if (!name) return true
    return !omit.has(name)
}

ExternalPlugin.Explorer({
    mapFn: explMapFn,
    filterFn: explFilterFn,
    order: ["filter", "map", "sort"],
})

const config = await loadQuartzConfig()
export default config
export const layout = await loadQuartzLayout()
