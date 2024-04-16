#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: cmake
# autospec version: v5
# autospec commit: c02b2fe
#
%define keepstatic 1
Name     : PDAL
Version  : 2.6.3
Release  : 25
URL      : https://github.com/PDAL/PDAL/releases/download/2.6.3/PDAL-2.6.3-src.tar.gz
Source0  : https://github.com/PDAL/PDAL/releases/download/2.6.3/PDAL-2.6.3-src.tar.gz
Summary  : Point Data Abstraction Library
Group    : Development/Tools
License  : BSD-3-Clause BSL-1.0 MIT
Requires: PDAL-bin = %{version}-%{release}
Requires: PDAL-data = %{version}-%{release}
Requires: PDAL-lib = %{version}-%{release}
Requires: PDAL-license = %{version}-%{release}
BuildRequires : buildreq-cmake
BuildRequires : cmake
BuildRequires : curl-dev
BuildRequires : gdal-dev
BuildRequires : git
BuildRequires : glibc-dev
BuildRequires : hdf5-dev
BuildRequires : libgeotiff-dev
BuildRequires : libxml2-dev
BuildRequires : openssl-dev
BuildRequires : pkgconfig(proj)
BuildRequires : postgresql-dev
BuildRequires : python3
BuildRequires : zlib-dev
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}

%description
https://github.com/connormanning/arbiter
To update the bundle:
cd <arbiter-location>
python amalgamate -c pdal
cp ./dist/* <pdal-location>/vendor/arbiter

%package bin
Summary: bin components for the PDAL package.
Group: Binaries
Requires: PDAL-data = %{version}-%{release}
Requires: PDAL-license = %{version}-%{release}

%description bin
bin components for the PDAL package.


%package data
Summary: data components for the PDAL package.
Group: Data

%description data
data components for the PDAL package.


%package dev
Summary: dev components for the PDAL package.
Group: Development
Requires: PDAL-lib = %{version}-%{release}
Requires: PDAL-bin = %{version}-%{release}
Requires: PDAL-data = %{version}-%{release}
Provides: PDAL-devel = %{version}-%{release}
Requires: PDAL = %{version}-%{release}

%description dev
dev components for the PDAL package.


%package lib
Summary: lib components for the PDAL package.
Group: Libraries
Requires: PDAL-data = %{version}-%{release}
Requires: PDAL-license = %{version}-%{release}

%description lib
lib components for the PDAL package.


%package license
Summary: license components for the PDAL package.
Group: Default

%description license
license components for the PDAL package.


%prep
%setup -q -n PDAL-2.6.3-src
cd %{_builddir}/PDAL-2.6.3-src

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1711741530
mkdir -p clr-build
pushd clr-build
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
CLEAR_INTERMEDIATE_CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS"
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS"
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS"
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS"
ASFLAGS="$CLEAR_INTERMEDIATE_ASFLAGS"
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS"
export GOAMD64=v2
%cmake .. -DWITH_COMPLETION=YES \
-DWITH_TESTS=NO
make  %{?_smp_mflags}
popd

%install
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
CLEAR_INTERMEDIATE_CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS"
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS"
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS"
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS"
ASFLAGS="$CLEAR_INTERMEDIATE_ASFLAGS"
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS"
export SOURCE_DATE_EPOCH=1711741530
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/PDAL
cp %{_builddir}/PDAL-%{version}-src/LICENSE.txt %{buildroot}/usr/share/package-licenses/PDAL/54963270ff2cf2308cfadb429224d1b173cdb3d1 || :
cp %{_builddir}/PDAL-%{version}-src/plugins/e57/libE57Format/LICENSE.md %{buildroot}/usr/share/package-licenses/PDAL/3cba29011be2b9d59f6204d6fa0a386b1b2dbd90 || :
cp %{_builddir}/PDAL-%{version}-src/plugins/e57/libE57Format/contrib/CRCpp/LICENSE %{buildroot}/usr/share/package-licenses/PDAL/b21021c423ae92368f44c6e018b81ce7436f9095 || :
cp %{_builddir}/PDAL-%{version}-src/vendor/arbiter/LICENSE %{buildroot}/usr/share/package-licenses/PDAL/fcb83a798bf5e65b4866c2b9addd70794f67083c || :
cp %{_builddir}/PDAL-%{version}-src/vendor/utfcpp/LICENSE %{buildroot}/usr/share/package-licenses/PDAL/3cba29011be2b9d59f6204d6fa0a386b1b2dbd90 || :
export GOAMD64=v2
GOAMD64=v2
pushd clr-build
%make_install
popd
## install_append content
# Cleanup permissions on header files
find %{buildroot}/usr/include -type f -exec chmod 644 {} +
## install_append end

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/pdal
/usr/bin/pdal-config

%files data
%defattr(-,root,root,-)
/usr/share/bash-completion/completions/pdal

%files dev
%defattr(-,root,root,-)
/usr/include/pdal/Artifact.hpp
/usr/include/pdal/ArtifactManager.hpp
/usr/include/pdal/DbReader.hpp
/usr/include/pdal/DbWriter.hpp
/usr/include/pdal/DimDetail.hpp
/usr/include/pdal/DimType.hpp
/usr/include/pdal/DimUtil.hpp
/usr/include/pdal/Dimension.hpp
/usr/include/pdal/Filter.hpp
/usr/include/pdal/FlexWriter.hpp
/usr/include/pdal/Geometry.hpp
/usr/include/pdal/JsonFwd.hpp
/usr/include/pdal/KDIndex.hpp
/usr/include/pdal/Kernel.hpp
/usr/include/pdal/Log.hpp
/usr/include/pdal/Mesh.hpp
/usr/include/pdal/Metadata.hpp
/usr/include/pdal/Options.hpp
/usr/include/pdal/PDALUtils.hpp
/usr/include/pdal/PipelineExecutor.hpp
/usr/include/pdal/PipelineManager.hpp
/usr/include/pdal/PipelineReaderJSON.hpp
/usr/include/pdal/PipelineWriter.hpp
/usr/include/pdal/PluginDirectory.hpp
/usr/include/pdal/PluginHelper.hpp
/usr/include/pdal/PluginInfo.hpp
/usr/include/pdal/PluginManager.hpp
/usr/include/pdal/PointContainer.hpp
/usr/include/pdal/PointLayout.hpp
/usr/include/pdal/PointRef.hpp
/usr/include/pdal/PointTable.hpp
/usr/include/pdal/PointView.hpp
/usr/include/pdal/Polygon.hpp
/usr/include/pdal/QuadIndex.hpp
/usr/include/pdal/QuickInfo.hpp
/usr/include/pdal/Reader.hpp
/usr/include/pdal/Scaling.hpp
/usr/include/pdal/SpatialReference.hpp
/usr/include/pdal/SrsBounds.hpp
/usr/include/pdal/Stage.hpp
/usr/include/pdal/StageExtensions.hpp
/usr/include/pdal/StageFactory.hpp
/usr/include/pdal/StageWrapper.hpp
/usr/include/pdal/Streamable.hpp
/usr/include/pdal/SubcommandKernel.hpp
/usr/include/pdal/Writer.hpp
/usr/include/pdal/XMLSchema.hpp
/usr/include/pdal/compression/Compression.hpp
/usr/include/pdal/compression/DeflateCompression.hpp
/usr/include/pdal/compression/GzipCompression.hpp
/usr/include/pdal/compression/LazPerfVlrCompression.hpp
/usr/include/pdal/compression/LzmaCompression.hpp
/usr/include/pdal/compression/ZstdCompression.hpp
/usr/include/pdal/filters/ApproximateCoplanarFilter.hpp
/usr/include/pdal/filters/AssignFilter.hpp
/usr/include/pdal/filters/CSFilter.hpp
/usr/include/pdal/filters/ChipperFilter.hpp
/usr/include/pdal/filters/ClusterFilter.hpp
/usr/include/pdal/filters/ColorInterpRamps.hpp
/usr/include/pdal/filters/ColorinterpFilter.hpp
/usr/include/pdal/filters/ColorizationFilter.hpp
/usr/include/pdal/filters/CovarianceFeaturesFilter.hpp
/usr/include/pdal/filters/CropFilter.hpp
/usr/include/pdal/filters/DBSCANFilter.hpp
/usr/include/pdal/filters/DEMFilter.hpp
/usr/include/pdal/filters/DecimationFilter.hpp
/usr/include/pdal/filters/DelaunayFilter.hpp
/usr/include/pdal/filters/DividerFilter.hpp
/usr/include/pdal/filters/ELMFilter.hpp
/usr/include/pdal/filters/EigenvaluesFilter.hpp
/usr/include/pdal/filters/EstimateRankFilter.hpp
/usr/include/pdal/filters/ExpressionFilter.hpp
/usr/include/pdal/filters/FaceRasterFilter.hpp
/usr/include/pdal/filters/FarthestPointSamplingFilter.hpp
/usr/include/pdal/filters/FerryFilter.hpp
/usr/include/pdal/filters/GeomDistanceFilter.hpp
/usr/include/pdal/filters/GeoreferenceFilter.hpp
/usr/include/pdal/filters/GpsTimeConvert.hpp
/usr/include/pdal/filters/GreedyProjection.hpp
/usr/include/pdal/filters/GroupByFilter.hpp
/usr/include/pdal/filters/HagDelaunayFilter.hpp
/usr/include/pdal/filters/HagDemFilter.hpp
/usr/include/pdal/filters/HagNnFilter.hpp
/usr/include/pdal/filters/HeadFilter.hpp
/usr/include/pdal/filters/HexBinFilter.hpp
/usr/include/pdal/filters/IQRFilter.hpp
/usr/include/pdal/filters/InfoFilter.hpp
/usr/include/pdal/filters/IterativeClosestPoint.hpp
/usr/include/pdal/filters/LOFFilter.hpp
/usr/include/pdal/filters/LiTreeFilter.hpp
/usr/include/pdal/filters/LloydKMeansFilter.hpp
/usr/include/pdal/filters/LocateFilter.hpp
/usr/include/pdal/filters/MADFilter.hpp
/usr/include/pdal/filters/MergeFilter.hpp
/usr/include/pdal/filters/MiniballFilter.hpp
/usr/include/pdal/filters/MongoExpressionFilter.hpp
/usr/include/pdal/filters/MortonOrderFilter.hpp
/usr/include/pdal/filters/NNDistanceFilter.hpp
/usr/include/pdal/filters/NeighborClassifierFilter.hpp
/usr/include/pdal/filters/NormalFilter.hpp
/usr/include/pdal/filters/OptimalNeighborhoodFilter.hpp
/usr/include/pdal/filters/OutlierFilter.hpp
/usr/include/pdal/filters/OverlayFilter.hpp
/usr/include/pdal/filters/PMFFilter.hpp
/usr/include/pdal/filters/PlaneFitFilter.hpp
/usr/include/pdal/filters/PoissonFilter.hpp
/usr/include/pdal/filters/ProjPipelineFilter.hpp
/usr/include/pdal/filters/RadialDensityFilter.hpp
/usr/include/pdal/filters/RandomizeFilter.hpp
/usr/include/pdal/filters/RangeFilter.hpp
/usr/include/pdal/filters/ReciprocityFilter.hpp
/usr/include/pdal/filters/RelaxationDartThrowing.hpp
/usr/include/pdal/filters/ReprojectionFilter.hpp
/usr/include/pdal/filters/ReturnsFilter.hpp
/usr/include/pdal/filters/SMRFilter.hpp
/usr/include/pdal/filters/SampleFilter.hpp
/usr/include/pdal/filters/SeparateScanLineFilter.hpp
/usr/include/pdal/filters/ShellFilter.hpp
/usr/include/pdal/filters/SkewnessBalancingFilter.hpp
/usr/include/pdal/filters/SortFilter.hpp
/usr/include/pdal/filters/SplitterFilter.hpp
/usr/include/pdal/filters/StatsFilter.hpp
/usr/include/pdal/filters/StraightenFilter.hpp
/usr/include/pdal/filters/StreamCallbackFilter.hpp
/usr/include/pdal/filters/TailFilter.hpp
/usr/include/pdal/filters/TransformationFilter.hpp
/usr/include/pdal/filters/VoxelCenterNearestNeighborFilter.hpp
/usr/include/pdal/filters/VoxelCentroidNearestNeighborFilter.hpp
/usr/include/pdal/filters/VoxelDownsizeFilter.hpp
/usr/include/pdal/filters/ZsmoothFilter.hpp
/usr/include/pdal/filters/private/DimRange.hpp
/usr/include/pdal/filters/private/Point.hpp
/usr/include/pdal/filters/private/Segmentation.hpp
/usr/include/pdal/filters/private/delaunator.hpp
/usr/include/pdal/filters/private/expr/AssignParser.hpp
/usr/include/pdal/filters/private/expr/AssignStatement.hpp
/usr/include/pdal/filters/private/expr/BaseParser.hpp
/usr/include/pdal/filters/private/expr/ConditionalExpression.hpp
/usr/include/pdal/filters/private/expr/ConditionalParser.hpp
/usr/include/pdal/filters/private/expr/Expression.hpp
/usr/include/pdal/filters/private/expr/IdentExpression.hpp
/usr/include/pdal/filters/private/expr/Lexer.hpp
/usr/include/pdal/filters/private/expr/MathExpression.hpp
/usr/include/pdal/filters/private/expr/MathParser.hpp
/usr/include/pdal/filters/private/expr/Token.hpp
/usr/include/pdal/filters/private/georeference/LocalCartesian.hpp
/usr/include/pdal/filters/private/georeference/Trajectory.hpp
/usr/include/pdal/filters/private/georeference/Utils.hpp
/usr/include/pdal/filters/private/hexer/HexGrid.hpp
/usr/include/pdal/filters/private/hexer/HexInfo.hpp
/usr/include/pdal/filters/private/hexer/HexIter.hpp
/usr/include/pdal/filters/private/hexer/Hexagon.hpp
/usr/include/pdal/filters/private/hexer/Mathpair.hpp
/usr/include/pdal/filters/private/hexer/Path.hpp
/usr/include/pdal/filters/private/hexer/Processor.hpp
/usr/include/pdal/filters/private/hexer/Segment.hpp
/usr/include/pdal/filters/private/hexer/exception.hpp
/usr/include/pdal/filters/private/mongoexpression/Comparison.hpp
/usr/include/pdal/filters/private/mongoexpression/Expression.hpp
/usr/include/pdal/filters/private/mongoexpression/LogicGate.hpp
/usr/include/pdal/filters/private/mongoexpression/Support.hpp
/usr/include/pdal/filters/private/pnp/Comparison.hpp
/usr/include/pdal/filters/private/pnp/Grid.hpp
/usr/include/pdal/filters/private/pnp/GridPnp.hpp
/usr/include/pdal/filters/private/pnp/VoxelRayTrace.hpp
/usr/include/pdal/filters/private/straighten/Polyline.hpp
/usr/include/pdal/filters/private/straighten/Utils.hpp
/usr/include/pdal/io/BpfCompressor.hpp
/usr/include/pdal/io/BpfHeader.hpp
/usr/include/pdal/io/BpfReader.hpp
/usr/include/pdal/io/BpfWriter.hpp
/usr/include/pdal/io/BufferReader.hpp
/usr/include/pdal/io/CopcReader.hpp
/usr/include/pdal/io/CopcWriter.hpp
/usr/include/pdal/io/EptAddonWriter.hpp
/usr/include/pdal/io/EptReader.hpp
/usr/include/pdal/io/EsriReader.hpp
/usr/include/pdal/io/FauxReader.hpp
/usr/include/pdal/io/FbiHeader.hpp
/usr/include/pdal/io/FbiReader.hpp
/usr/include/pdal/io/FbiWriter.hpp
/usr/include/pdal/io/GDALReader.hpp
/usr/include/pdal/io/GDALWriter.hpp
/usr/include/pdal/io/GltfWriter.hpp
/usr/include/pdal/io/HeaderVal.hpp
/usr/include/pdal/io/I3SReader.hpp
/usr/include/pdal/io/Ilvis2MetadataReader.hpp
/usr/include/pdal/io/Ilvis2Reader.hpp
/usr/include/pdal/io/LasHeader.hpp
/usr/include/pdal/io/LasReader.hpp
/usr/include/pdal/io/LasVLR.hpp
/usr/include/pdal/io/LasWriter.hpp
/usr/include/pdal/io/MemoryViewReader.hpp
/usr/include/pdal/io/NullWriter.hpp
/usr/include/pdal/io/OGRWriter.hpp
/usr/include/pdal/io/ObjReader.hpp
/usr/include/pdal/io/OptechCommon.hpp
/usr/include/pdal/io/OptechReader.hpp
/usr/include/pdal/io/OptechRotationMatrix.hpp
/usr/include/pdal/io/PcdHeader.hpp
/usr/include/pdal/io/PcdReader.hpp
/usr/include/pdal/io/PcdWriter.hpp
/usr/include/pdal/io/PlyReader.hpp
/usr/include/pdal/io/PlyWriter.hpp
/usr/include/pdal/io/PtsReader.hpp
/usr/include/pdal/io/PtxReader.hpp
/usr/include/pdal/io/QfitReader.hpp
/usr/include/pdal/io/RasterWriter.hpp
/usr/include/pdal/io/SbetCommon.hpp
/usr/include/pdal/io/SbetReader.hpp
/usr/include/pdal/io/SbetSmrmsgReader.hpp
/usr/include/pdal/io/SbetWriter.hpp
/usr/include/pdal/io/SlpkReader.hpp
/usr/include/pdal/io/StacReader.hpp
/usr/include/pdal/io/TIndexReader.hpp
/usr/include/pdal/io/TerrasolidReader.hpp
/usr/include/pdal/io/TextReader.hpp
/usr/include/pdal/io/TextWriter.hpp
/usr/include/pdal/io/point_types.hpp
/usr/include/pdal/io/private/GDALGrid.hpp
/usr/include/pdal/io/private/connector/Connector.hpp
/usr/include/pdal/io/private/copc/Entry.hpp
/usr/include/pdal/io/private/copc/Info.hpp
/usr/include/pdal/io/private/copc/Key.hpp
/usr/include/pdal/io/private/copc/Tile.hpp
/usr/include/pdal/io/private/copcwriter/BuPyramid.hpp
/usr/include/pdal/io/private/copcwriter/CellManager.hpp
/usr/include/pdal/io/private/copcwriter/Common.hpp
/usr/include/pdal/io/private/copcwriter/Grid.hpp
/usr/include/pdal/io/private/copcwriter/GridKey.hpp
/usr/include/pdal/io/private/copcwriter/OctantInfo.hpp
/usr/include/pdal/io/private/copcwriter/Output.hpp
/usr/include/pdal/io/private/copcwriter/Processor.hpp
/usr/include/pdal/io/private/copcwriter/PyramidManager.hpp
/usr/include/pdal/io/private/copcwriter/Reprocessor.hpp
/usr/include/pdal/io/private/copcwriter/VoxelInfo.hpp
/usr/include/pdal/io/private/copcwriter/VoxelKey.hpp
/usr/include/pdal/io/private/ept/Addon.hpp
/usr/include/pdal/io/private/ept/Artifact.hpp
/usr/include/pdal/io/private/ept/EptInfo.hpp
/usr/include/pdal/io/private/ept/EptSupport.hpp
/usr/include/pdal/io/private/ept/FixedPointLayout.hpp
/usr/include/pdal/io/private/ept/Key.hpp
/usr/include/pdal/io/private/ept/Overlap.hpp
/usr/include/pdal/io/private/ept/TileContents.hpp
/usr/include/pdal/io/private/ept/VectorPointTable.hpp
/usr/include/pdal/io/private/esri/EsriUtil.hpp
/usr/include/pdal/io/private/esri/Obb.hpp
/usr/include/pdal/io/private/esri/PageManager.hpp
/usr/include/pdal/io/private/las/Geotiff.hpp
/usr/include/pdal/io/private/las/Header.hpp
/usr/include/pdal/io/private/las/Srs.hpp
/usr/include/pdal/io/private/las/Summary.hpp
/usr/include/pdal/io/private/las/Utils.hpp
/usr/include/pdal/io/private/las/Vlr.hpp
/usr/include/pdal/io/private/stac/Catalog.hpp
/usr/include/pdal/io/private/stac/Collection.hpp
/usr/include/pdal/io/private/stac/Item.hpp
/usr/include/pdal/io/private/stac/ItemCollection.hpp
/usr/include/pdal/io/private/stac/Utils.hpp
/usr/include/pdal/kernels/ChamferKernel.hpp
/usr/include/pdal/kernels/DeltaKernel.hpp
/usr/include/pdal/kernels/DensityKernel.hpp
/usr/include/pdal/kernels/EvalKernel.hpp
/usr/include/pdal/kernels/GroundKernel.hpp
/usr/include/pdal/kernels/HausdorffKernel.hpp
/usr/include/pdal/kernels/InfoKernel.hpp
/usr/include/pdal/kernels/MergeKernel.hpp
/usr/include/pdal/kernels/PipelineKernel.hpp
/usr/include/pdal/kernels/RandomKernel.hpp
/usr/include/pdal/kernels/SortKernel.hpp
/usr/include/pdal/kernels/SplitKernel.hpp
/usr/include/pdal/kernels/TIndexKernel.hpp
/usr/include/pdal/kernels/TileKernel.hpp
/usr/include/pdal/kernels/TranslateKernel.hpp
/usr/include/pdal/kernels/private/PointlessLas.hpp
/usr/include/pdal/kernels/private/density/OGR.hpp
/usr/include/pdal/kernels/private/stac/StacInfo.hpp
/usr/include/pdal/pdal.hpp
/usr/include/pdal/pdal_config.hpp
/usr/include/pdal/pdal_export.hpp
/usr/include/pdal/pdal_features.hpp
/usr/include/pdal/pdal_internal.hpp
/usr/include/pdal/pdal_test_main.hpp
/usr/include/pdal/pdal_types.hpp
/usr/include/pdal/private/DynamicLibrary.hpp
/usr/include/pdal/private/KDImpl.hpp
/usr/include/pdal/private/MathUtils.hpp
/usr/include/pdal/private/Raster.hpp
/usr/include/pdal/private/SrsTransform.hpp
/usr/include/pdal/private/StageRunner.hpp
/usr/include/pdal/private/gdal/ErrorHandler.hpp
/usr/include/pdal/private/gdal/GDALError.hpp
/usr/include/pdal/private/gdal/GDALUtils.hpp
/usr/include/pdal/private/gdal/Raster.hpp
/usr/include/pdal/private/gdal/SpatialRef.hpp
/usr/include/pdal/util/Algorithm.hpp
/usr/include/pdal/util/Backtrace.hpp
/usr/include/pdal/util/Bounds.hpp
/usr/include/pdal/util/Charbuf.hpp
/usr/include/pdal/util/Extractor.hpp
/usr/include/pdal/util/FileUtils.hpp
/usr/include/pdal/util/Georeference.hpp
/usr/include/pdal/util/IStream.hpp
/usr/include/pdal/util/Inserter.hpp
/usr/include/pdal/util/NullOStream.hpp
/usr/include/pdal/util/OStream.hpp
/usr/include/pdal/util/ProgramArgs.hpp
/usr/include/pdal/util/Random.hpp
/usr/include/pdal/util/ThreadPool.hpp
/usr/include/pdal/util/Utils.hpp
/usr/include/pdal/util/Uuid.hpp
/usr/include/pdal/util/pdal_util_export.hpp
/usr/include/pdal/util/pdal_util_internal.hpp
/usr/include/pdal/util/portable_endian.hpp
/usr/include/pdal/util/private/BacktraceImpl.hpp
/usr/lib64/cmake/PDAL/PDALConfig.cmake
/usr/lib64/cmake/PDAL/PDALConfigVersion.cmake
/usr/lib64/cmake/PDAL/PDALTargets-relwithdebinfo.cmake
/usr/lib64/cmake/PDAL/PDALTargets.cmake
/usr/lib64/cmake/PDAL/pluginmacros.cmake
/usr/lib64/libpdal_plugin_kernel_fauxplugin.so
/usr/lib64/libpdal_plugin_reader_pgpointcloud.so
/usr/lib64/libpdal_plugin_writer_pgpointcloud.so
/usr/lib64/libpdalcpp.so
/usr/lib64/pkgconfig/pdal.pc

%files lib
%defattr(-,root,root,-)
/usr/lib64/libpdal_plugin_kernel_fauxplugin.so.16
/usr/lib64/libpdal_plugin_kernel_fauxplugin.so.16.3.0
/usr/lib64/libpdal_plugin_reader_pgpointcloud.so.16
/usr/lib64/libpdal_plugin_reader_pgpointcloud.so.16.3.0
/usr/lib64/libpdal_plugin_writer_pgpointcloud.so.16
/usr/lib64/libpdal_plugin_writer_pgpointcloud.so.16.3.0
/usr/lib64/libpdalcpp.so.16
/usr/lib64/libpdalcpp.so.16.3.0

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/PDAL/3cba29011be2b9d59f6204d6fa0a386b1b2dbd90
/usr/share/package-licenses/PDAL/54963270ff2cf2308cfadb429224d1b173cdb3d1
/usr/share/package-licenses/PDAL/b21021c423ae92368f44c6e018b81ce7436f9095
/usr/share/package-licenses/PDAL/fcb83a798bf5e65b4866c2b9addd70794f67083c
